from __future__ import annotations

import datetime
import inspect
import json
import multiprocessing
import os
import pathlib
import pickle
import sys

# from contextlib import redirect_stderr
from copy import deepcopy
from dataclasses import dataclass, field, fields
from io import StringIO
from typing import Any, Callable, Generic, TypeVar, overload

import pandas as pd
import requests  # type: ignore
import tqdm

# from wurlitzer import pipes  # type: ignore
import wurlitzer
import xarray as xr
from adi_py import ADILogger, Process, SkipProcessingIntervalException  # type: ignore
from adi_py.utils import is_empty_function  # type: ignore
from mock import patch  # type: ignore

# out = StringIO()
T = TypeVar("T", bound="Process")  # for AdiProcess


@dataclass
class AdiRunner:
    process_name: str

    # TODO: Should these be arguments to run()? If so, then we'd need to handle the
    # input_datasets / output_datasets slightly differently

    site: str
    facility: str
    begin_date: str
    end_date: str

    pcm_link: str | None = field(default=None, init=False, repr=True)

    DATASTREAM_DATA_IN: str | None = field(
        default_factory=lambda: os.getenv("DATASTREAM_DATA_IN"),
        repr=False,
    )
    DATASTREAM_DATA_OUT: str | None = field(
        default_factory=lambda: os.getenv("DATASTREAM_DATA_OUT"),
        repr=False,
    )
    QUICKLOOK_DATA: str | None = field(
        default_factory=lambda: os.getenv("QUICKLOOK_DATA"),
        repr=False,
    )
    LOGS_DATA: str | None = field(
        default_factory=lambda: os.getenv("LOGS_DATA"),
        repr=False,
    )
    CONF_DATA: str | None = field(
        default_factory=lambda: os.getenv("CONF_DATA"),
        repr=False,
    )
    ADI_PY_MODE: str | None = field(
        default_factory=lambda: os.getenv("ADI_PY_MODE"),
        repr=False,
    )

    ADI_TMP_DIR: str | None = field(
        default_factory=lambda: os.getenv("ADI_TMP_DIR"),
        repr=False,
    )

    # Also TODO: is there a way we can send the output data files into the abyss? E.g.,
    # set output data to /dev/null or /tmp or something like that? We have the data in
    # memory, so we don't need it on disk unless the user wants it there.

    # Maybe this should also be in the repr?
    process_class: type[Process] = field(default=Process, repr=False)

    # TODO: Create Protocol/more accurate type hints for each hook function
    init_process_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    pre_retrieval_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    post_retrieval_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    pre_transform_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    post_transform_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    process_data_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    finish_process_hook: Callable | None = field(default=None, repr=False, kw_only=True)
    quicklook_hook: Callable | None = field(default=None, repr=False, kw_only=True)

    def __post_init__(self):
        # Configure ADI Environment variables,
        self._setup_environment_variables()
        self._init_dataset_store()

        self.wrapped_adi_process: Process = create_adi_process(self)
        self.multiprocessing_controller = MultiProcessingController(runner=self)

        self.pcm_process = PcmProcess(self.process_name)

        self.retrieval_rule_sets = self.pcm_process.retrieval_rule_sets
        self.output_datastreams = self.pcm_process.output_datastreams
        self.coordinate_systems = self.pcm_process.coordinate_systems

        self.pcm_link = f"https://pcm.arm.gov/pcm/process/{self.process_name}"
        self.pcm_revision_number = self.pcm_process.revision_number

        # Note: invalid site-facility and date are fed into sys.args and will crash notebook.
        self._validate_pcm_site_facility()
        self._validate_date()

        self.pickle_path = f"{self.ADI_TMP_DIR}/{self.process_name}"

        self._data_consolidate_mode: bool = False  # data_consolidate or VAP

        self.process_status: ProcessStatus = ProcessStatus("")  # per run

    def _init_dataset_store(self):
        self._input_datasets: list[dict[str, xr.Dataset | None]] = []
        self._output_datasets: list[dict[str, xr.Dataset | None]] = []
        self._transformed_datasets: list[dict[str, xr.Dataset | None]] = []

        self._process_intervals: list[dict[str, tuple[int, int]]] = []

        # _input_datasets refactor to tabular
        init_df: pd.DataFrame = pd.DataFrame(
            {
                "datastream": pd.Series(dtype=str),
                "time_start": pd.Series(
                    dtype=object
                ),  # TODO: discuss which timestamp type to use
                "time_end": pd.Series(dtype=object),
                "dataset_id": pd.Series(dtype=int),
                "dataset_info": pd.Series(dtype=object),
            }
        )
        self._input_dataset_table = init_df.copy(deep=True)
        self._output_dataset_table = init_df.copy(deep=True)
        self._transformed_dataset_table = init_df.copy(deep=True)

        self._input_dataset_dict: dict[int, xr.Dataset] = {}
        self._output_dataset_dict: dict[int, xr.Dataset] = {}
        self._transformed_dataset_dict: dict[int, xr.Dataset] = {}

    def _setup_environment_variables(self):
        """Helper function to setup env var,
        Precedence : Valid API, Existing Env Vars, Reasonable Default.
        Then update the instance fields accordingly"""

        adi_env_var_default = {
            "DATASTREAM_DATA_IN": "/data/archive",
            "DATASTREAM_DATA_OUT": f'/data/home/{os.environ["USER"]}/data/datastream',
            "QUICKLOOK_DATA": f'/data/home/{os.environ["USER"]}/data/quicklook',
            "LOGS_DATA": f'/data/home/{os.environ["USER"]}/data/logs',
            "CONF_DATA": f'/data/home/{os.environ["USER"]}/data/conf',
            "ADI_PY_MODE": "development",
            "ADI_TMP_DIR": f'/home/{os.environ["USER"]}/.adi_tmp',
        }

        for name, value in adi_env_var_default.items():
            existing_runner_value = getattr(self, name, None)
            if existing_runner_value is not None:
                value = existing_runner_value
            self._validate_environment_variable(name=name, value=value)
            os.environ[name] = value
            setattr(self, name, value)  # update fields

    def _validate_environment_variable(self, name: str, value: str):
        if name == "ADI_PY_MODE":
            adi_py_modes = ["development", "production"]
            if value not in adi_py_modes:
                raise ValueError(
                    f"Invalid env_var {name}={value}. Not in {adi_py_modes}."
                )
        elif name == "DATASTREAM_DATA_IN":
            if not os.access(value, os.R_OK):
                raise ValueError(
                    f"Invalid env_var {name}={value}. Path does not exist or have Read Permissions."
                )
        else:
            if not os.path.exists(value):
                try:
                    os.makedirs(value, exist_ok=True)
                    assert os.access(value, os.W_OK)
                except Exception as e:
                    print(e)
                    raise ValueError(
                        f"Invalid env_var {name}={value}. Path does not have Write Permissions."
                    )

    def _validate_pcm_site_facility(self):
        if (self.site, self.facility) not in self.pcm_process.site_facilities:
            raise ValueError(
                f"(site, facility): ({self.site}, {self.facility})"
                f"is not in the defined pcm site_facilities {self.pcm_process.site_facilities}. (case-sensitive.)"
            )

    def to_datetime(self, date: str, format: str = "%Y%m%d") -> datetime.datetime:
        try:
            assert len(date) == 8
            return datetime.datetime.strptime(date, format)
        except ValueError or AssertionError:
            raise ValueError(
                f'Invalid date={date}. Needs to be a valid date in the "%Y%m%d" format.(e.g., 20200101.).'
            )

    def _validate_date(self):
        if not self.to_datetime(self.begin_date) and (
            self.to_datetime(self.begin_date) < datetime.datetime(1992, 1, 1)
        ):
            raise ValueError(
                f"begin_date={self.begin_date} is less than the earliest ARM data=19920101."
            )
        if not self.to_datetime(self.end_date) and (
            self.to_datetime(self.end_date) < self.to_datetime(self.begin_date)
        ):
            raise ValueError(
                f"end_date={self.end_date} is earlier than the begin_date={self.begin_date}."
            )

    @property
    def data_consolidate_mode(self):
        return self._data_consolidate_mode

    def run_data_consolidator(
        self,
        debug_level: int = 2,
        show_progressbar: bool = True,
        show_logs: bool = False,
        smart_cache: bool = True,
    ) -> ProcessStatus:
        self._data_consolidate_mode = True
        self._validate_run_args(debug_level, show_progressbar, show_logs, smart_cache)
        return self._run()

    def run_vap(
        self,
        debug_level: int = 2,
        show_progressbar: bool = True,
        show_logs: bool = False,
        smart_cache: bool = True,
    ) -> ProcessStatus:
        self._data_consolidate_mode = False
        self._validate_run_args(debug_level, show_progressbar, show_logs, smart_cache)
        return self._run()

    def _validate_run_args(
        self,
        debug_level: int = 2,
        show_progressbar: bool = True,
        show_logs: bool = False,
        smart_cache: bool = True,
    ):
        assert debug_level in [0, 1, 2]
        if show_logs and show_progressbar:
            method_name = type(self.process_status).logs.fget.__name__  # type: ignore
            print(
                f"Warning: Conflicting setting {show_logs=} and {show_progressbar=}. Changed to show_logs=False.\n"
                f"Note: You can view logs with the `{method_name}` property method "
                f"of the returned `{self.process_status.__class__.__name__}` object. e.g., print(status.{method_name})"
            )
            show_logs = False

        # TODO: clean up the following attributes (maybe put into a container)
        self.run_debug_level = debug_level
        self.run_smart_cache = smart_cache
        self.run_show_logs = show_logs
        self.run_show_progressbar = show_progressbar

    def _run_per_processing_interval_is_day(self) -> str:
        ...
        # when per_processing_interval == 86400, break down start - end into per day
        date_list = pd.date_range(
            self.to_datetime(self.begin_date), self.to_datetime(self.end_date), freq="D"
        )
        date_list_bound = [
            (dt, dt + pd.DateOffset()) for dt in date_list[:-1]
        ]  # skip end_date
        date_list_bound_str = [
            (dt1.strftime("%Y%m%d"), dt2.strftime("%Y%m%d"))
            for (dt1, dt2) in date_list_bound
        ]
        proc_args = (
            ["-n", self.process_name]
            if len(self.wrapped_adi_process.process_names) > 1
            else []
        )
        logs: str = ""
        for begin_date, end_date in tqdm.tqdm(
            date_list_bound_str, disable=not self.run_show_progressbar
        ):
            # for begin_date, end_date in date_list_bound_str:
            # TODO: discuss how necessary it is to use a patch for the sys.args. (We need to install extra lib mock)
            # Special concern is when there is multiprocessing jobs, the sys.argv can be conflicting.
            # args = [
            sys.argv = [
                os.path.realpath(__file__),  # not actually needed
                *proc_args,
                "-s",
                self.site,
                "-f",
                self.facility,
                "-b",
                begin_date,
                "-e",
                end_date,
                "-D",
                f"{self.run_debug_level}",
                "-R",
                "--dynamic-dods",
            ]
            with wurlitzer.pipes() as (out, _):
                self.wrapped_adi_process.run()
            log = str(out.read())
            if self.run_show_logs:
                # print(log)
                print(self.process_status._patch_cache_logs(log))
            logs += log
        return logs

    def _run(self) -> ProcessStatus:
        self._init_dataset_store()
        self.process_status = ProcessStatus("", self.data_consolidate_mode)

        # TODO: discuss the use cases of multiple process_name, it conflicts the current model which assumes single pcm process
        proc_args = (
            ["-n", self.process_name]
            if len(self.wrapped_adi_process.process_names) > 1
            else []
        )

        # TODO: discuss how necessary it is to use a patch for the sys.args. (We need to install extra lib mock)
        # args = [
        sys.argv = [
            os.path.realpath(__file__),  # not actually needed
            *proc_args,
            "-s",
            self.site,
            "-f",
            self.facility,
            "-b",
            self.begin_date,
            "-e",
            self.end_date,
            "-D",
            f"{self.run_debug_level}",
            "-R",
            "--dynamic-dods",
        ]

        # Note: experiment with run jobs if output_interval == processing_interval == 86400
        if self.pcm_process.processing_interval == 86400:
            intervals = [
                v["interval"] for k, v in self.pcm_process.output_intervals.items()
            ]
            timezones = [
                v["timezone"] for k, v in self.pcm_process.output_intervals.items()
            ]
            if [e is None for e in intervals] and [e is None for e in timezones]:
                logs = self._run_per_processing_interval_is_day()
        else:
            msg = f"Status Unknown. Please check logs at {self.LOGS_DATA}."
            print(f"Warning: {msg}")
            self.wrapped_adi_process.run()
            logs = msg
        self.process_status.update_logs(logs)
        return self.process_status

    def _empty_datastore_warning(self):
        if self.data_consolidate_mode:
            method_name = self.run_data_consolidator.__name__
        else:
            method_name = self.run_vap.__name__
        print(
            f"Warning: If empty, call  {method_name}{inspect.signature(self._run)} to process data first."
        )

    @property
    def input_datasets(self) -> DataStore:
        if not self._input_datasets:
            self._empty_datastore_warning()
        return DataStore(self._input_datasets, self._process_intervals)

    @property
    def output_datasets(self) -> DataStore:
        if not self._output_datasets:
            self._empty_datastore_warning()
        return DataStore(self._output_datasets, self._process_intervals)

    @property
    def transformed_datasets(self) -> DataStore:
        if not self._transformed_datasets:
            self._empty_datastore_warning()
        return DataStore(self._transformed_datasets, self._process_intervals)


@dataclass
class PcmProcess:
    """Tracks some information of a PCM Process Definition."""

    process_name: str
    pcm_link: str | None = field(default=None, init=False, repr=True)
    _process_info: dict | None = field(default=None, init=True, repr=False)
    _revision_number: int | None = field(default=None, init=True, repr=False)

    def __post_init__(self):
        self.pcm_link = f"https://pcm.arm.gov/pcm/process/{self.process_name}"
        self._validate_pcm_name()

    def _validate_pcm_name(self):
        if self.process_name not in PcmProcess._existing_processes():
            raise ValueError(
                f'PCM process: "{self.process_name}" is not in the records.'
            )

    def _verify_pcm_api_schema(self): ...  # TODO: verify pcm api schema

    @property
    def process_info(self) -> dict:
        if self._process_info:
            return self._process_info
        else:
            return self.get_update_process_info()

    def get_update_process_info(self) -> dict:
        url = f"https://pcm.arm.gov/pcm/api/processes/{self.process_name}"
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Could not connect to PCM Process API {url}")
            raise ConnectionError(f"Could not connect to PCM Process API '{url}'")
        try:
            self._process_info = res.json()["process"]
            return self._process_info
        except:
            print(
                "An error occurred while attempting to interpret the process definition for"
                f" {self.process_name}. Please ensure the process name is valid."
            )
            raise

    @property
    def revision_number(self):
        if self._revision_number:
            return self._revision_number
        url = f"https://pcm.arm.gov/pcm/api/processes/{self.process_name}/revisions"
        res = requests.get(url)

        if res.status_code != 200:
            print(f"Could not connect to PCM Process API {url}")
            raise ConnectionError(f"Could not connect to PCM Process API '{url}'")
        try:
            self._revision_number = res.json()[-1]["rev_num"]
            return self._revision_number
        except:
            print(
                "An error occurred while attempting to interpret the process definition for"
                f" {self.process_name}. Please ensure the process name is valid."
            )
            raise

    @property
    def existing_processes(self):
        return self._existing_processes()

    @staticmethod
    def _existing_processes() -> list[str]:
        url = "https://pcm.arm.gov/pcm/api/processes"
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Could not connect to PCM Process API {url}")
            raise ConnectionError(f"Could not connect to PCM Process API '{url}'")
        return list(res.json().keys())

    @property
    def retrieval_rule_sets(self) -> list[str]:
        process_info = self.process_info
        return list(process_info["variable_retrieval"]["input_datasets"].keys())

    @property
    def input_datastreams(self) -> list[str]:
        process_info = self.process_info
        return process_info["input_datastreams"]

    @property
    def output_datastreams(self) -> list[str]:
        process_info = self.process_info
        return process_info["output_datastreams"]

    @property
    def coordinate_systems(self) -> list[str]:
        process_info = self.process_info
        return list(process_info["variable_retrieval"]["coordinate_systems"].keys())

    @property
    def site_facilities(self) -> list[tuple[str, str]]:
        # Note: case sensitive: site: lowercase, facility: uppercase
        return [
            (location["site"].lower(), location["fac"].upper())
            for location in self._run_locations
        ]

    @property
    def processing_interval(self) -> int:
        processing_interval = int(self.process_info["processing_interval"])
        if processing_interval != 86400:
            print(
                f"Warning: {processing_interval =} != 86400. This is not recommended."
            )
        return processing_interval

    @property
    def output_intervals(self) -> dict[str, dict[str, str | int | None]]:
        """
        EXA<PLE:
        {'adimappedgrid.c1': {'interval': None, 'timezone': None},
        'adiregulargrid.c1': {'interval': None, 'timezone': None},
        'nocoord.c1': {'interval': None, 'timezone': None},
        'nocoord2.c1': {'interval': None, 'timezone': None},
        'testing.c0': {'interval': None, 'timezone': None}}"""
        return self.process_info["output_interval"]

    @property
    def _run_locations(self) -> list[dict[str, str]]:
        process_info = self.process_info
        return process_info["run_locations"]

    # @property
    # def overview(self) -> pd.DataFrame:
    #     return self.get_pcm_plans()

    @property
    def retrieval_rule_set_priorities(self) -> dict[str, dict[int, str]]:
        """
        EXAMPLE:
        {'ceil_b1': {1: 'ceil.b1'},
        'met_b1': {1: 'met.b1', 2: 'met.b1'},
        'twrmr_c1': {1: '1twrmr.c1', 2: 'sirs.b1'}}"""
        df_rules = self._get_filtered_retrieval_rule_set_rules()
        priorities = {}
        for input_dataset, rule in zip(
            df_rules["retrieval_rule_set"].values,
            df_rules.rules.values,
        ):
            priorities[input_dataset] = {
                x["priority"]: x["datastream_name"] for x in rule
            }
        return priorities

    @property
    def mapping_priorities(self) -> dict[tuple[str, str], dict[int, str]]:
        """
        EXAMPLE:
        {('ceil_b1', 'half_min_grid'): {1: 'ceil.b1'},
        ('ceil_b1', 'mapped'): {1: 'ceil.b1'},
        ('met_b1', 'half_min_grid'): {1: 'met.b1', 2: 'met.b1'},
        ('met_b1', None): {1: 'met.b1', 2: 'met.b1'},
        ('twrmr_c1', 'mapped'): {1: '1twrmr.c1', 2: 'sirs.b1'}}"""
        df_rules = self._get_mapping_rules()
        priorities = {}
        for input_dataset, coordinate_system, rule in zip(
            df_rules["retrieval_rule_set"].values,  # TODO: need schema verification
            df_rules.coordinate_system.values,
            df_rules.rules.values,
        ):
            priorities[(input_dataset, coordinate_system)] = {
                x["priority"]: x["datastream_name"] for x in rule
            }
        return priorities

    @property
    def _transform_mappings(self) -> dict[str, str]:
        mappings = {}
        for input_dataset, coords in zip(
            self._get_transform_mappings().input_dataset.values,
            self._get_transform_mappings().coordinate_system.values,
        ):
            mappings[input_dataset] = coords
        return mappings

    def _get_output_mappings(self) -> pd.DataFrame:
        process = self.process_info
        df_stacked = pd.DataFrame(
            process["variable_retrieval"]["output_datastream_variable_mappings"]
        ).stack()
        df_var_output_mapping = df_stacked.reset_index()
        df_var_output_mapping.columns = [
            "variable",
            "output_datastream",
            "variable_out",
        ]  # non-standard names
        return pd.merge(
            df_var_output_mapping,
            pd.DataFrame(
                {"output_datastream": self.output_datastreams},
            ),
            how="outer",
        )

    def _get_retrieved_variables(self, rich_info: bool = False) -> pd.DataFrame:
        process = self.process_info
        df_var = pd.DataFrame(process["variable_retrieval"]["retrieved_variables"]).T
        df_var.index.name = "variable"  # non-standard names
        df_var = df_var.reset_index().sort_values("input_dataset")
        df_var = df_var.drop("name", axis=1).rename(
            lambda x: "retrieval_rule_set" if x == "input_dataset" else x,
            axis="columns",
        )
        if rich_info:
            return df_var
        else:
            return df_var[["variable", "retrieval_rule_set", "coordinate_system"]]

    def get_retrieval_rules(
        self, rich_info: bool = True, pivot: bool = True
    ) -> pd.DataFrame:
        if rich_info:
            df_retrieval_rule_set_rules = self._get_full_retrieval_rules()
        else:
            df_retrieval_rule_set_rules = self._get_filtered_retrieval_rules()

        df_retrieval_rule_set_rules_normalized = pd.concat(
            [
                df_retrieval_rule_set_rules.explode("rules").reset_index(drop=True),
                pd.json_normalize(
                    df_retrieval_rule_set_rules.explode("rules").rules,  # type: ignore
                    max_level=0,
                ),
            ],
            axis=1,
        ).drop("rules", axis=1)
        df_retrieval_rule_set_rules_normalized = (
            df_retrieval_rule_set_rules_normalized.sort_values(
                ["retrieval_rule_set", "priority"]
            )
        )
        if pivot:
            return self._pivot_df_by(
                df_retrieval_rule_set_rules_normalized,
                "retrieval_rule_set",
                index_within_group=True,
            )
        else:
            return df_retrieval_rule_set_rules_normalized

    @staticmethod
    def filter_dict(
        datastream: dict,
    ):
        filtered = [
            {
                key: datastream_dict[key]
                for key in [
                    "priority",
                    "datastream_name",
                    # "run_location",
                    # "run_time",,
                    # "data_location"
                ]
            }
            for datastream_dict in datastream
        ]
        return sorted(filtered, key=lambda d: d["priority"])

    def _get_full_retrieval_rules(self) -> pd.DataFrame:
        process = self.process_info
        return pd.DataFrame(
            pd.DataFrame(process["variable_retrieval"]["input_datasets"]).T["rules"]
        ).reset_index(names="retrieval_rule_set")

    def _get_filtered_retrieval_rules(self) -> pd.DataFrame:
        df = self._get_full_retrieval_rules()
        df["rules"] = df.rules.apply(self.filter_dict)
        return df

    def _get_filtered_retrieval_rule_set_rules(self) -> pd.DataFrame:
        df_filtered_retrieval_rules = self._get_filtered_retrieval_rules()
        df_filtered_retrieval_rules["input_datastreams"] = (
            df_filtered_retrieval_rules.rules.apply(
                lambda x: list(set([rule["datastream_name"] for rule in x]))
            )
        )
        return df_filtered_retrieval_rules

    def _get_mapping_rules(self):
        df_rules = self._get_filtered_retrieval_rule_set_rules()
        df_vars = self._get_retrieved_variables()

        return pd.merge(
            df_rules,
            df_vars,
            how="inner",
            on="retrieval_rule_set",
        ).drop("variable", axis=1)

    def _get_transform_mappings(self):
        df_rules = self._get_filtered_retrieval_rule_set_rules()
        df_vars = self._get_retrieved_variables()
        df_mappings = (
            df_vars.groupby("input_dataset")["coordinate_system"]
            .apply(list)
            .reset_index()
        )
        df_mappings["coordinate_system_nona"] = df_mappings.coordinate_system.apply(
            lambda x: [coord for coord in x if coord]
        )
        return pd.merge(
            df_rules,
            df_mappings,
            how="left",
            on="input_dataset",
        )

    def get_pcm_overview(
        self, pivot_by_col: str = "retrieval_rule_set"
    ) -> pd.DataFrame:
        """pivot_by_col in [
            "retrieval_rule_set",
            "coordinate_system",
            "output_datastream",
            "no_pivot"
        ]"""
        assert pivot_by_col in [
            "retrieval_rule_set",
            "coordinate_system",
            "output_datastream",
            "no_pivot",
        ]
        df = self._get_pcm_overview()
        if pivot_by_col == "no_pivot":
            return df
        elif pivot_by_col == "output_datastream":
            return self._pivot_df_by(
                df.explode(pivot_by_col),  # type: ignore
                pivot_by_col,
                index_within_group=True,
            )
        else:
            return self._pivot_df_by(df, pivot_by_col)

    @staticmethod
    def _pivot_df_by(
        df: pd.DataFrame, col: str, index_within_group: bool = False
    ) -> pd.DataFrame:
        df_pivot = df.copy()
        df_pivot = df_pivot.sort_values(col).reset_index(drop=True)
        if not index_within_group:
            single_index = df_pivot.index
        else:
            single_index = pd.Index(
                df_pivot.fillna("NA").groupby(col).cumcount().values
            )
        tuples = zip(df_pivot[col], single_index)
        index = pd.MultiIndex.from_tuples(
            tuples,
            names=[col, single_index.name],
        )
        df_pivot.index = index
        df_pivot = df_pivot.drop([col], axis=1)
        return df_pivot

    def _get_pcm_overview(self) -> pd.DataFrame:
        df_var_non_rich = self._get_retrieved_variables()
        df_output_mapping = (
            self._get_output_mappings()
            .groupby("variable")
            .output_datastream.apply(list)
            .reset_index()
        )
        df_input_dataset_rules_non_normalized = (
            self._get_filtered_retrieval_rule_set_rules()
        )

        df_merge_1 = pd.merge(
            df_var_non_rich, df_output_mapping, how="outer", on="variable"
        )
        df_merge_2 = pd.merge(
            df_merge_1,
            df_input_dataset_rules_non_normalized,
            how="outer",
            on="retrieval_rule_set",
        )

        return (
            df_merge_2[
                [
                    "retrieval_rule_set",
                    "coordinate_system",
                    "variable",
                    "output_datastream",
                    "rules",
                ]
            ]
            .sort_values(["retrieval_rule_set", "coordinate_system", "variable"])
            .reset_index(drop=True)
        )


class DataStore:
    # TODO: future: support .shape, .keys, length, etc.
    def __init__(
        self,
        data: list[dict[str, xr.Dataset | None]],
        ts: list[dict[str, tuple[int, int]]] = [],
    ):
        self.data = data
        self.ts = ts

    def __getitem__(self, key: int | str) -> DataSubStore:
        # TODO: future: support slicing
        if isinstance(key, int):
            return self.by_interval(key)
        elif isinstance(key, str):
            return self.by_datastream(key)
        else:
            raise

    def by_datastream(self, name: str) -> DataSubStore:
        # return [x[name] for x in self.data]
        return DataSubStore(
            [x[name] for x in self.data], [x["ts"] for x in self.ts], name
        )

    def by_interval(self, index: int) -> DataSubStore:
        # return self.data[index]
        return DataSubStore(self.data[index], self.ts[index], index)

    def _per_interval_repr(
        self,
        ts_dict: dict[str, tuple[int, int]],
        data_dict: dict[str, xr.Dataset | None],
    ):
        ts_tuple = list(ts_dict.values())[0]
        start = datetime.datetime.fromtimestamp(ts_tuple[0]).strftime("%Y-%m-%d")
        end = datetime.datetime.fromtimestamp(ts_tuple[1]).strftime("%Y-%m-%d")
        time_stamp_line = "\t" + f"{start}--> {end}" + "\t{"

        dataset_lines: list[str] = []
        for datastream, ds in data_dict.items():
            # dim_info = ", ".join([f"{k}: {v}" for k, v in ds.sizes.items()])
            dataset_lines += [
                "\t\t" + f"{datastream}: {XarrayDatasetRepr.one_line_repr(ds)},"
            ]

        close_line = "\t}"

        return [time_stamp_line] + dataset_lines + [close_line]

    def __repr__(self):
        """
        EXAMPLE:
        DataStore
        [
            <0/2> 	2022-01-01--> 2022-01-02	{
                adimappedgrid.c1: xr.Dataset(time: 1440, bound: 2),
                adiregulargrid.c1: xr.Dataset(time: 48, range: 8000, bound: 2),
                nocoord.c1: xr.Dataset(time: 1440, bound: 2),
                nocoord2.c1: xr.Dataset(time: 1440, bound: 2),
            }
            <1/2> 	2022-01-02--> 2022-01-03	{
                adimappedgrid.c1: xr.Dataset(time: 1440, bound: 2),
                adiregulargrid.c1: xr.Dataset(time: 48, range: 8000, bound: 2),
                nocoord.c1: xr.Dataset(time: 1440, bound: 2),
                nocoord2.c1: xr.Dataset(time: 1440, bound: 2),
            }
            <2/2> 	2022-01-03--> 2022-01-04	{
                adimappedgrid.c1: xr.Dataset(time: 1440, bound: 2),
                adiregulargrid.c1: xr.Dataset(time: 48, range: 8000, bound: 2),
                nocoord.c1: xr.Dataset(time: 1440, bound: 2),
                nocoord2.c1: xr.Dataset(time: 1440, bound: 2),
            }
        ]
        """
        open_lines = "DataStore\n["

        dataset_lines = []
        for i, (interval, data) in enumerate(zip(self.ts, self.data)):
            per_interval_repr = self._per_interval_repr(interval, data)
            per_interval_repr[0] = (
                "\t" + f"<{i}/{len(self.ts) - 1}+1> " + per_interval_repr[0]
            )
            # dataset_lines += per_interval_repr(interval, data)
            if i < 2 or (i == 2 and len(self.ts) <= 3):
                dataset_lines += per_interval_repr
            elif i == len(self.ts) - 1:
                dataset_lines += ["\n\t...\n"]
                dataset_lines += per_interval_repr

        close_line = "]"

        return "\n".join([open_lines] + dataset_lines + [close_line])


class DataSubStore:
    # TODO: future: support .shape, .keys, length, etc.
    def __init__(self, data_slice, ts_slice, key):
        self.data_slice: list[xr.Dataset] | dict[str, xr.Dataset] = data_slice
        self.ts_slice: list[tuple[int, int]] | dict[str, tuple[int, int]] = ts_slice
        self.key: str | int = key

    @staticmethod
    def _index_timestamp_expression(
        index: int, last_index: int, start: int, end: int
    ) -> str:
        if last_index < 0:
            total_str = " "
        else:
            total_str = last_index
        t_start = datetime.datetime.fromtimestamp(start).strftime("%Y-%m-%d")
        t_end = datetime.datetime.fromtimestamp(end).strftime("%Y-%m-%d")
        return f"<{index}/{total_str}+1>" + "\t" + f"{t_start}--> {t_end}"

    def _dict_like_repr(self):
        """
        EXAMPLE
        DataStore (interval=	<0/ >	2020-04-01--> 2020-04-02)
        {
            co2flx25m_b1: xr.Dataset(time: 48, bound: 2),
            swats_b1: xr.Dataset(time: 48, depth: 6),
        }
        """
        if (
            isinstance(self.ts_slice, dict)
            and isinstance(self.data_slice, dict)
            and isinstance(self.key, int)
        ):
            ts_slice: dict[str, tuple[int, int]] = self.ts_slice
            data_slice: dict[str, xr.Dataset] = self.data_slice
            key: int = self.key
        ts_tuple = list(ts_slice.values())[0]
        time_stamp_line = self._index_timestamp_expression(
            key,
            -1,
            ts_tuple[0],
            ts_tuple[1],
        )
        open_lines = [f"DataStore (interval=\t{time_stamp_line}) \n" + "{"]
        repr_body = [
            "\t" + f"{datastream}: {XarrayDatasetRepr.one_line_repr(ds)},"
            for datastream, ds in data_slice.items()
        ]

        close_line = ["}"]
        return open_lines + repr_body + close_line

    def _list_like_repr(self):
        """
        EXAMPLE:
        DataStore (datastream=	co2flx25m_b1)
        [
            <0/4>	2020-04-01--> 2020-04-02	xr.Dataset(time: 48, bound: 2),
            <1/4>	2020-04-02--> 2020-04-03	xr.Dataset(time: 48, bound: 2),

            ...

            <4/4>	2020-04-05--> 2020-04-06	xr.Dataset(time: 48, bound: 2),
        ]
        """

        if (
            isinstance(self.ts_slice, list)
            and isinstance(self.data_slice, list)
            and isinstance(self.key, str)
        ):
            ts_slice: list[tuple[int, int]] = self.ts_slice
            data_slice: list[xr.Dataset] = self.data_slice
            key: str = self.key
        open_lines = [f"DataStore (datastream=\t{key}) \n["]
        repr_body = []
        for i, (ts, ds) in enumerate(zip(ts_slice, data_slice)):
            per_interval_repr = [
                "\t"
                + self._index_timestamp_expression(
                    i,
                    len(self.data_slice) - 1,
                    ts[0],
                    ts[1],
                )
                + "\t"
                + XarrayDatasetRepr.one_line_repr(ds)
                + ","
            ]
            if i < 2 or (i == 2 and len(self.ts_slice) <= 3):
                repr_body += per_interval_repr
            elif i == len(self.ts_slice) - 1:
                repr_body += ["\n\t...\n"]
                repr_body += per_interval_repr
        close_line = ["]"]
        return open_lines + repr_body + close_line

    def __repr__(self):
        if isinstance(self.data_slice, list):
            return "\n".join(self._list_like_repr())
        else:
            return "\n".join(self._dict_like_repr())

    def __getitem__(self, key: int | str) -> xr.Dataset:
        # TODO: future: support slicing
        if isinstance(self.data_slice, dict) and isinstance(key, str):
            return self.data_slice[key]
        elif isinstance(self.data_slice, list) and isinstance(key, int):
            return self.data_slice[key]
        raise


class XarrayDatasetRepr:
    @staticmethod
    def one_line_repr(ds: xr.Dataset | None):
        if ds is not None:
            dim_info = ", ".join([f"{k}: {v}" for k, v in ds.sizes.items()])
            return f"xr.Dataset({dim_info})"
        else:
            return "NA"

    @staticmethod
    def get_xrdataset_info(ds: xr.Dataset):
        # TODO: discuss what other fundamental info should be put here
        attr_dod_version = {"dod_version": ds.attrs["dod_version"]}
        xr_dataset_info: dict = {
            # "time range": (str(ds.time.data[0]).split(".")[0],str(ds.time.data[-1]).split(".")[0]),
            "time range": f'({str(ds.time.data[0]).split(".")[0]}, {str(ds.time.data[-1]).split(".")[0]})',
            "Coordinates": str(list(ds.coords)),
            "Data variables": str(list(ds.data_vars)),
        }
        xr_dataset_info.update(attr_dod_version)
        return xr_dataset_info


class ProcessStatus:
    """Basic class representing the final process state."""

    def __init__(
        self, logs: str = "", data_consolidate_mode: bool = False
    ):  # TODO: it feels odd to init data_consolidate_mode. redesign the workflow
        self._logs = logs
        self._data_consolidate_mode = data_consolidate_mode

    #     def _modify_cache_status(self):
    #         msg = """
    # ================================================================================
    # Suggested exit value: 0 (successful). (In data consolidate mode, skipping ALL the processing intervals is Not a failure situation.)
    # ================================================================================
    # """
    #         len_skip = self._n_expr(expr="SKIP PROCESSING INTERVAL", target=self.logs)
    #         len_proc = self._n_expr(expr="ENTERING PROCESS DATA HOOK", target=self.logs)
    #         if (
    #             self._data_consolidate_mode
    #             and len_skip > 0
    #             and len_skip == len_proc
    #             and msg not in self.logs
    #         ):
    #             self._logs += msg

    def _n_expr(self, expr: str, target: str):
        """Helper function to count how many expression appears in logs."""
        return len([line for line in target.splitlines() if expr in line])

    def _patch_cache_logs(self, old_logs: str) -> str:
        """Patch the suggested exit value when skipping ALL the processing intervals.
        This is not a failure situation, e.g., In data consolidate mode"""
        old_msg = "Suggested exit value: 1 (failure)"
        patched_msg = (
            "//Status modified due to caching// Suggested exit value: 0 (successful)"
        )
        len_skip = self._n_expr(expr="SKIP PROCESSING INTERVAL", target=old_logs)
        len_proc = self._n_expr(expr="ENTERING PROCESS DATA HOOK", target=old_logs)
        if self._data_consolidate_mode and len_skip > 0 and len_skip == len_proc:
            return "\n".join(
                [line.replace(old_msg, patched_msg) for line in old_logs.splitlines()]
            )
        return old_logs

    @property
    def succeeded(self) -> bool | None:
        if self._logs:
            final_log_lines = "\n".join(self._logs.splitlines()[-5:])
        else:
            final_log_lines = ""
        if "successful" in final_log_lines:
            return True
        elif "Status Unknown" in final_log_lines:
            return None
        else:
            return False

    @property
    def logs(self) -> str:
        return self._logs

    def __repr__(self) -> str:
        if self.succeeded:
            status = "Success"
        elif self.succeeded is None:
            status = "Unknown"
        else:
            status = "Failed"
        return f"ProcessStatus={status}"

    def __bool__(self) -> bool | None:
        return self.succeeded

    def update_logs(self, logs: str) -> str:
        self._logs += self._patch_cache_logs(
            logs
        )  # TODO: using private method. consider redesign workflow.
        return self.logs


def invoke_parent_hook(
    process: Process,
    runner: AdiRunner,
    hook_name: str,
    *hook_args: Any,
    **hook_kwargs: Any,
) -> None:
    # The hook provided to AdiRunner()
    runner_hook = getattr(runner, hook_name, None)

    # The hook defined in the provided adi_py.Process subclass
    process_class_hook = getattr(runner.process_class, hook_name)

    if runner_hook is None:
        process_class_hook(process, *hook_args, **hook_kwargs)
        return None
    elif not is_empty_function(process_class_hook):
        class_name = runner.process_class.__class__
        warning_msg = (
            f"Warning! The provided process_class '{class_name}' implements {hook_name}"
            f", but {hook_name} was also provided as an argument to AdiRunner(). The"
            f" AdiRunner() hook will be used, and the {class_name} hook will be"
            " discarded."
        )
        print(warning_msg)
    runner_hook(process, *hook_args, **hook_kwargs)
    return None


def create_adi_process(runner: AdiRunner) -> Process:
    class AdiProcess(Process):
        def __init__(self):
            super().__init__()
            if (
                runner.process_class == Process
            ):  # TODO: discuss why we need to check runner.process_class to init, and how to init for not Process?
                self._process_names = [runner.process_name]
                self._include_debug_dumps = False

            self.current_interval: int = -1

        def init_process_hook(self):
            invoke_parent_hook(self, runner, "init_process_hook")

        def pre_retrieval_hook(self, begin_date: int, end_date: int):
            self.current_interval += 1
            invoke_parent_hook(self, runner, "pre_retrieval_hook", begin_date, end_date)

        def post_retrieval_hook(self, begin_date: int, end_date: int):
            # Note: if no input data found per processing interval.
            # ADI would not enter the remaining hooks including this one.
            # print(
            #     f'====== enter post_retrieval_hook {begin_date =}'
            #     f'{datetime.datetime.fromtimestamp(begin_date).strftime("%Y-%m-%d")}'
            # )
            invoke_parent_hook(
                self, runner, "post_retrieval_hook", begin_date, end_date
            )

        def pre_transform_hook(self, begin_date: int, end_date: int):
            # Note: dsproc_merge_data hook can merge multiple data per interval, u
            # thus better to retrieve input data in this hook to avoid handing get_retrieved_dataset vs. get_retrieved_datasets.
            # ref: https://engineering.arm.gov/ADI_doc/algorithm.html?highlight=process%20model#dsproc-main

            invoke_parent_hook(self, runner, "pre_transform_hook", begin_date, end_date)
            interval_data: dict[str, xr.Dataset | None] = {}

            file_name = ProcessCacher.get_pickle_name(
                pcm=runner.process_name,
                version=f"v{runner.pcm_revision_number}",
                site=runner.site,
                facility=runner.facility,
                start=begin_date,
                end=end_date,
                type="input",
            )
            abs_file = ProcessCacher.get_abs_path(
                parent_path=runner.pickle_path, file_name=file_name
            )
            if os.path.exists(abs_file) and runner.run_smart_cache:
                interval_data = ProcessCacher.load_ds(abs_file=abs_file)
                ADILogger.info(
                    f"Skipping processing interval because using caching and { file_name = } exists."
                )
                # TODO: discuss the skip mechanism. Note: when using SkipProcessingIntervalException the whole interval will be skipped. (i.e., no later hook will be called)
                # Note: argue that the most expensive calculation is the self.get_retrieved_dataset, self.get_transformed_dataset procedure, it improves performance even only cache that part. (cut time in half)
                # With the current design, focus on cache consolidate data, i.e., with no custom hook.
                # Note: ADI still save some output data to the local system even cached, that's some efficiency to improve.
                # return
                # raise SkipProcessingIntervalException(
                #     f"Skipping processing interval because using caching and { file_name = } exists."
                # )
            else:
                for (
                    input_dataset,
                    priorities,
                ) in runner.pcm_process.retrieval_rule_set_priorities.items():
                    input_datastreams = priorities.values()
                    for ds_name in input_datastreams:
                        ds = self.get_retrieved_dataset(ds_name)
                        if ds is not None:
                            ds = ds.copy(deep=True)
                            interval_data[input_dataset] = ds
                            break  # Break for datastream with lower priority
                if interval_data.get(input_dataset) is None:
                    interval_data[input_dataset] = None  # place holder
                ProcessCacher.dump_ds(abs_file=abs_file, var=interval_data)

            runner._input_datasets.append(interval_data)

            # TODO: here is the candidate place holder to directly inject custom code,
            # to access it, use runner._input_datasets[index].
            # Note: runner.input_datasets might not be available at this moment,
            # since process_interval is not available until the later process hook.

            # TODO: add and verify sync process

        def post_transform_hook(self, begin_date: int, end_date: int):
            # Note: Automatically establishing transformed plan from PCM is feasible and efficient, since
            # ADI is sophisticated enough to only transformed variables that assigned to certain coordinate system.
            # For example,
            #   - for variable_x and of variable_y retrieved from input_dataset_1,
            #   - variable_x is transformed by coordinate_a, variable_y of is transformed by coordinate_b,
            #   - variable_x would only appear in input_dataset_1+=>coordinate_a but not in input_dataset_1+=>coordinate_b, and similar to variable_y.
            invoke_parent_hook(
                self, runner, "post_transform_hook", begin_date, end_date
            )
            interval_data: dict[str, xr.Dataset | None] = {}

            file_name = ProcessCacher.get_pickle_name(
                pcm=runner.process_name,
                version=f"v{runner.pcm_revision_number}",
                site=runner.site,
                facility=runner.facility,
                start=begin_date,
                end=end_date,
                type="transformed",
            )
            abs_file = ProcessCacher.get_abs_path(
                parent_path=runner.pickle_path, file_name=file_name
            )
            if os.path.exists(abs_file) and runner.run_smart_cache:
                interval_data = ProcessCacher.load_ds(abs_file=abs_file)
                ADILogger.info(
                    f"Skipping processing interval because using caching and { file_name = } exists."
                )
                # TODO: discuss the skip mechanism. Note: when using SkipProcessingIntervalException the whole interval will be skipped. (i.e., no later hook will be called)
                # Note: argue that the most expensive calculation is the self.get_retrieved_dataset, self.get_transformed_dataset procedure, it improves performance even only cache that part.
                # With the current design, focus on cache consolidate data, i.e., with no custom hook.
                # Note: ADI still save some output data to the local system even cached, that's some efficiency to improve.
                # return
                # raise SkipProcessingIntervalException(
                #     f"Skipping processing interval because using caching and { file_name = } exists."
                # )
            else:
                for (
                    (input_dataset, coordinate_system),
                    priorities,
                ) in runner.pcm_process.mapping_priorities.items():
                    input_datastreams = priorities.values()
                    # for coordinate_system in runner.pcm_process.transform_mappings[input_dataset]:
                    if coordinate_system is None:
                        continue
                    mapping_name = f"{input_dataset}+=>{coordinate_system}"
                    for ds_name in input_datastreams:
                        ds = self.get_transformed_dataset(ds_name, coordinate_system)
                        if ds is not None:
                            ds = ds.copy(deep=True)

                            interval_data[mapping_name] = ds
                            break  # Break for datastream with lower priority
                if interval_data.get(mapping_name) is None:
                    interval_data[mapping_name] = None  # place holder
                ProcessCacher.dump_ds(abs_file=abs_file, var=interval_data)

            runner._transformed_datasets.append(interval_data)

        def process_data_hook(self, begin_date: int, end_date: int):
            invoke_parent_hook(self, runner, "process_data_hook", begin_date, end_date)
            interval_data: dict[str, xr.Dataset | None] = {}

            file_name = ProcessCacher.get_pickle_name(
                pcm=runner.process_name,
                version=f"v{runner.pcm_revision_number}",
                site=runner.site,
                facility=runner.facility,
                start=begin_date,
                end=end_date,
                type="output",
            )
            abs_file = ProcessCacher.get_abs_path(
                parent_path=runner.pickle_path, file_name=file_name
            )
            if os.path.exists(abs_file) and runner.run_smart_cache:
                interval_data = ProcessCacher.load_ds(abs_file=abs_file)
                ADILogger.info(
                    f"Skipping processing interval because using caching and { file_name = } exists."
                )
                # TODO: discuss the skip mechanism. Note: when using SkipProcessingIntervalException the whole interval will be skipped. (i.e., no later hook will be called)
                # Note: argue that the most expensive calculation is the self.get_retrieved_dataset, self.get_transformed_dataset procedure, it improves performance even only cache that part.
                # With the current design, focus on cache consolidate data, i.e., with no custom hook.
                # Note: ADI still save some output data to the local system even cached, that's some efficiency to improve.
                # return

            else:
                for ds_name in runner.output_datastreams:
                    ds = self.get_output_dataset(ds_name)
                    if ds is not None:
                        ds = ds.copy(deep=True)
                        interval_data[ds_name] = ds
                    else:
                        interval_data[ds_name] = ds
                ProcessCacher.dump_ds(abs_file=abs_file, var=interval_data)
            runner._output_datasets.append(interval_data)
            runner._process_intervals.append({"ts": (begin_date, end_date)})
            if runner.data_consolidate_mode:
                raise SkipProcessingIntervalException(
                    f"Skipping processing interval because using caching and { file_name = } exists."
                )

        def quicklook_hook(self, begin_date: int, end_date: int):
            invoke_parent_hook(self, runner, "quicklook_hook", begin_date, end_date)

        def finish_process_hook(self):
            invoke_parent_hook(self, runner, "finish_process_hook")

    return AdiProcess()


class ProcessCacher:
    @staticmethod
    def get_pickle_name(
        pcm: str,
        version: str,
        site: str,
        facility: str,
        start: int,
        end: int,
        type: str,
    ):
        """
        encoded pickle name that can identify if a process is run on consolidator per process interval."""
        # TODO: adding function encoding to tell if certain custom hook is injected and if the content has changed.
        return f"{pcm}_{version}_{site}_{facility}_{start}_{end}_{type}.pickle"

    @staticmethod
    def get_abs_path(parent_path: str, file_name: str):
        return os.path.join(parent_path, file_name)

    @staticmethod
    def dump_ds(abs_file: str, var: dict[str, xr.Dataset | None]):
        # parent_path = pathlib.Path(abs_file).parents[0]
        # if not os.path.exists(parent_path):
        #     os.makedirs(parent_path, exist_ok=True)
        # Note: abs_file parent path is validated.
        with open(abs_file, "wb+") as f:
            pickle.dump(var, f)

    @staticmethod
    def load_ds(abs_file: str) -> dict[str, xr.Dataset | None]:
        try:
            with open(abs_file, "rb+") as f:
                var = pickle.load(f)
            return var
        except Exception as e:
            print(e)
            # Don't skip silently
            raise e

    @classmethod
    def clean_cache(cls): ...  # TODO


class MultiProcessingController(multiprocessing.Process):
    def __init__(self, runner: AdiRunner) -> None:
        super().__init__()
        self.wrapped_adi_process: Process = create_adi_process(runner)

    def run(
        self,
    ):
        return self.wrapped_adi_process.run()
