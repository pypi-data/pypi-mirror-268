from __future__ import annotations
# **********************************************************************************************************************
#  Author:
#     name:  None
#     phone: None
#     email: None
# **********************************************************************************************************************

import numpy as np
import sys
import xarray as xr

import dsproc3 as dsproc
from adi_py import Process, ADILogger, SkipProcessingIntervalException
# from .version import __version__
import uuid
import pickle
import pathlib
from pathlib import Path
import os

import requests
import copy
import subprocess

import argparse
from typing import List, Dict, Set, Any, Tuple
from functools import reduce
import json

from collections.abc import Iterable
from collections.abc import Mapping

import pandas as pd

from copy import deepcopy



    
class AdiDatasetList(list):
    """
    A data class to wrap the List[Dict[str, xr.Dataset]]
    e.g., self._ds_ins: List[Dict[str, xr.Dataset]] = []  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
    Since xr.Dataset is not very print friendly
    """

    def __init__(self, iterable):
        self.iterable = iterable
        iterable = [AdiDatasetDict(i) for i in iterable if iterable]
        super().__init__(iterable)

    def __repr__(self):
        if self is []:
            return super().__repr__()
        
        iterable = deepcopy(self.iterable)
        for ds_per_iteration in iterable:
            # ds_per_iteration = AdiDatasetDict(ds_per_iteration)
            for k, v in ds_per_iteration.items():
                ds_per_iteration[k] = PrettyXarrayDataset(v)
                # ds_per_iteration[k] = xr.Dataset(v)
        return iterable.__repr__()


class AdiDatasetDict(dict):
    """
    A data class to wrap the Dict[str, xr.Dataset]
    e.g., self._ds_ins: Dict[str, xr.Dataset] = {}  # {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}
    Since xr.Dataset is not very print friendly
    """
    def __init__(self, dictionary):
        self.dictionary = dictionary
        super().__init__(dictionary)

    def __repr__(self):
        """
        EXAMPLE:
        {'met.b1': <XarrayDataset>({
            "Coordinates": "['time']",
            "Data variables": "['alt', 'lat', 'lon', 'met_temperature', 'qc_met_temperature']",
            "dod_version": "met-b1-7.3"
        })}
        """
        if self is {}:
            return super().__repr__()
        
        dictionary = deepcopy(self.dictionary)
        for k, v in dictionary.items():
            dictionary[k] = PrettyXarrayDataset(v)
            # ds_per_iteration[k] = xr.Dataset(v)
        return dictionary.__repr__()

# class DatastreamToDatasetMap(dict):
    
#     def __repr__(self) -> str:
#         # should only be one item in the map
#         key = list(self.keys())[0]
#         ds = list(self.values())[0]

#         start, end = ds["time"].data[0], ds["time"].data[-1]
#         return f"\{{key}: xr.Dataset(time=slice({start},{end}))\}"


# from xarray.core.formatting import *
# from xarray.core.formatting import _calculate_col_width, _get_boolean_with_default
DataVars = Mapping[Any, Any]
class PrettyXarrayDataset(xr.Dataset):
    """
    Pretty printing xr.Dataset"""
    
    # def __init__(self, ds: xr.Dataset):
    #     super().__init__(ds)

    def __init__(self, 
                 ds: xr.Dataset,                                                                                                                                        
                 # could make a VariableArgs to use more generally, and refine these
                 # categories
                
    ) -> None:
        data_vars = ds.data_vars       
        coords = ds.coords
        attrs = ds.attrs
        super().__init__(data_vars = data_vars,      
                         coords = coords,
                         attrs = attrs)

    # TODO: got warning 
    # "FutureWarning: xarray subclass PrettyXarrayDataset should explicitly define __slots__  cls = super().__new__(mcls, name, bases, namespace, **kwargs)"
    # TODO: check xtending xarray using accessors: https://docs.xarray.dev/en/latest/internals/extending-xarray.html
    def __repr__(self):
        # return self.dataset_repr(self)
        # self.attrs = super().attrs
        # print("super().attrs")
        # print(super().attrs)
        return f"<XarrayDataset>" + "(" + json.dumps(self.get_xrdataset_info(), indent=4)+ ")"

    def get_xrdataset_info(self):
        # TODO: discuss what other fundamental info should be put here
        attr_command_line = {"command_line": self.attrs["command_line"] }
        attr_dod_version = {"dod_version": self.attrs["dod_version"] }
        xr_dataset_info: dict = {
            "time range": (str(self.time.data[0]).split(".")[0],str(self.time.data[-1]).split(".")[0]),
            "Coordinates": str(list(self.coords)),
            "Data variables": str(list(self.data_vars)),            
            } 
        xr_dataset_info.update(attr_dod_version)
        return xr_dataset_info


class ProcessStatus:
    """Basic class representing the final process state."""

    def __init__(self, logs: str):
        self._logs = logs

    @property
    def succeeded(self) -> bool:
        final_log_lines = "\n".join(self._logs.splitlines()[-5:])
        return "successful" in final_log_lines

    @property
    def logs(self) -> str:
        return self._logs
    
    def __repr__(self) -> str:
        return "Success" if self.succeeded else "Failed"

    def __bool__(self) -> bool:
        return self.succeeded
        

class AdiRunner:  # TODO: better name?
    # TODO: docstring

    def __init__(self, pcm_name: str, site: str, facility: str, begin_date: str, end_date: str):
        """TODO: write a docstring

        Args:
            pcm_name (str): The PCM Process name, e.g., 'aosccnsmpskappa'
            site (str): The site where you want to run the process at.
            facility (str): The facility you want to run the process at.
            begin_date (str): The begin date of the process as a YYYYMMDD string.
            end_date (str): The end date of the process as a YYYYMMDD string.
        """

        self._adi_process = ADI_Process(
            pcm_name=pcm_name,
            site=site,
            facility=facility,
            begin_date=begin_date,
            end_date=end_date
        )
        """A wrapper around adi_py.Process which allows for the Process to be run in a jupyter notebook."""

        self.site = site
        self.facility = facility
        self.begin_date = begin_date
        self.end_date = end_date
        self.pcm_name = pcm_name


    def process(self, cached: bool = False, verbose: bool = True) -> ProcessStatus:
        """Runs the process and creates retrieved, pre-transformed, post-transformed, and output datasets.

        Args:
            cached (bool, optional): TODO: write some text for this. Need to indicate how the cache works, limitations, etc. Defaults to False.
            verbose (bool, optional): Flag to enable logging from ADI. Defaults to True.

        Returns:
            ProcessStatus: True if the processing succeeded, False if an error occurred.
        """
        # TODO: the process method should capture and return the logs as a string
        logs = self._adi_process.process(cached=cached)
        status = ProcessStatus(logs)
        if verbose:
            print(status.logs)
        return status

    @property
    def input_datasets(self) -> list[dict[str, xr.Dataset]]:
        # TODO: docstring
        filepath = Path(self._adi_process.ds_ins_full_path)
        if not filepath.is_file():
            raise OSError(f"{filepath} does not exist. Run process() first.")
        data = self._adi_process._pickle_load_ds(filepath)
        return AdiDatasetList(data)
    
    @property
    def output_datasets(self) -> list[dict[str, xr.Dataset]]:
        # TODO: docstring
        filepath = Path(self._adi_process.ds_outs_full_path)
        if not filepath.is_file():
            raise OSError(f"{filepath} does not exist. Run process() first.")
        data = self._adi_process._pickle_load_ds(filepath)
        return AdiDatasetList(data)
    
    @property
    def transformed_datasets(self) -> list[dict[str, xr.Dataset]]:
        # TODO: docstring
        filepath = Path(self._adi_process.ds_transforms_full_path)
        if not filepath.is_file():
            raise OSError(f"{filepath} does not exist. Run process() first.")
        data = self._adi_process._pickle_load_ds(filepath)
        return AdiDatasetList(data)


class ADI_Process(Process):
    """-----------------------------------------------------------------------------------------------------------------
    This class implements the pblhtdlrf_training_validation process using the new, XArray-based ADI library.  Please see
    https://adi-python.readthedocs.io/en/latest/examples.html for more examples on how to use this API.
    -----------------------------------------------------------------------------------------------------------------"""

    MISSING_VALUE = -9999
    ADI_TMP_DIR = pathlib.Path(f'{os.getenv("HOME")}/.adi_tmp/')
    ADI_DATA_DIR = pathlib.Path(f'{os.getenv("HOME")}/.adi_tmp/data/')

    # Input datastreams
    # DS_IN_CO2FLX25M_B1 = 'co2flx25m.b1'
    # DS_IN_DLPROFWSTATS4NEWS_C1 = 'dlprofwstats4news.c1'
    # DS_IN_MET_B1 = 'met.b1'
    # DS_IN_PBLHTSONDE1MCFARL_C1 = 'pblhtsonde1mcfarl.c1'
    # DS_IN_STAMP_B1 = 'stamp.b1'
    # DS_IN_SWATS_B1 = 'swats.b1'
    
    # Output datastreams
    # DS_OUT_KMPBLHTDLRF_C1 = 'kmpblhtdlrftraining.c0'
    
    # Coordinate systems
    
    def __init__(self, pcm_name, site, facility, begin_date, end_date, **kwargs):
        """-------------------------------------------------------------------------------------------------------------
        Class constructor for PblhtdlrfTrainingValidation.  This method is used to initialize user data variables and main process
        settings that are stored within this class.  It is invoked BEFORE the dsproc main loop, so DO NOT call any
        init_process_hook methods here or you will likely get a segmentation fault error.
        -------------------------------------------------------------------------------------------------------------"""
        super().__init__()
        # self._process_names = ['pblhtdlrf_training_validation']
        self._process_names = [pcm_name]
        self._process_model = dsproc.PM_TRANSFORM_VAP
        self._process_version = "__version__"
        self._rollup_qc = True            # Roll up the qc bits of all vars with transformed qc bits in the output DOD
        self._include_debug_dumps = True  # This will automatically dump files if debug level > 1

        self._pcm_name = pcm_name
        self._site = site
        self._facility = facility
        self._begin_date, self._end_date = begin_date, end_date

        self._ds_str_flags: Dict[str, Set[int]] = dict()  # dict-like data structure to store set flags, e.g., {'co2flx25m.b1': set(dsproc.DS_STANDARD_QC, dsproc.DS_FILTER_NANS)}
        self._ds_int_flags: Dict[str, int] = dict() # dict-like data structure to store set flags, e.g., {'co2flx25m.b1': 10, 'dlprofwstats4news.c1': 2 }

        # get process info
        self.process_info: dict = self.retrieve_process(self._pcm_name) 
        # get input datastream name(s)
        self.ds_in_names = self.get_input_datastreams(self.process_info)
        # get output datastream name(s)
        self.ds_out_names = self.get_output_datastreams(self.process_info)
        # get transform name(s)
        self.coord_names = self.get_coordinate_systems(self.process_info)
        
        self._ds_ins: List[Dict[str, xr.Dataset]] = []  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        self._ds_transforms: List[Dict[str, xr.Dataset]] = []  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        self._ds_outs: List[Dict[str, xr.Dataset]] =  []  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        
        # self._ds_ins: AdiDataset = AdiDataset([])  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        # self._ds_transforms: AdiDataset = AdiDataset([])  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        # self._ds_outs: AdiDataset = AdiDataset([])  # [{'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}, {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2},]
        
        # TODO: make the structure of self.ds_ins and self.ds_outs more readable, 
        # proposing adding processing interval in-front
        # {
        #   {"HH:mm:ss-HH:mm:ss": {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}},
        #   {"HH:mm:ss-HH:mm:ss": {'co2flx25m.b1': ds1, 'dlprofwstats4news.c1': ds2}},
        #   ...
        # }
        # TODO: discuss the path conention: <userhome>/.adi_tmp/<pcm-name>/ 
        # and file convention: <process_name>_<site>_<facility>_<begin_date>_<end_date>.pickle
        self.pickle_path = pathlib.Path(f'{self.ADI_TMP_DIR}/{self._pcm_name}')
        # self.ds_ins_pickle_name = f"ds_ins_{self._pcm_name}_{self._site}_{self._facility}_{self._begin_date}_{self._end_date}.pickle"
        # self.ds_outs_pickle_name = f"ds_outs_{self._pcm_name}_{self._site}_{self._facility}_{self._begin_date}_{self._end_date}.pickle"

        # environment variables
        self._adi_env_vars = {}
        self.config_adi_env_vars()

        # # transformation plan
        # transform_pairs = self._get_all_transformation_pairs()
        self._transform_pairs: List[Tuple[str,str]] = []  # e.g., [('1twrmr.c1', 'mapped'), ('ceil.b1', 'half_min_grid')]

    def get_pcm_info(self):
        # TODO: discuss what other fundamental info should be put here
        # TODO: get PCM version !!!
        pcm_info: dict = {
            "pcm_name": self._pcm_name,
            "input_datastreams": self.ds_in_names,
            "output_datastreams": self.ds_out_names,
            "coordinates": self.coord_names,
            "datastream_flags": list(self.ds_str_flags),
            "valid_transformation_pairs": self.get_valid_transform_mappings(display_like_str=True)
        } 
        # pcm_info.update({"ENV-VARS": self._adi_env_vars})
        return pcm_info

    def get_pcm_info_as_table(self) ->pd.DataFrame:
        """
        Get a tabular formated PCM info
        EXAMPLE:
              group          shape             out_ds                 out_var  \
        0   ceil_b1  half_min_grid  adiregulargrid.c1        ceil_backscatter   
        1   ceil_b1         mapped                                              
        2   ceil_b1  half_min_grid  adiregulargrid.c1  ceil_laser_temperature   
        3    met_b1  half_min_grid  adiregulargrid.c1         met_temperature   
        4  twrmr_c1         mapped   adimappedgrid.c1       twrmr_temperature   

                             name           dims                 in_ds  
        0        ceil_backscatter  [time, range]             {ceil.b1}  
        1          ceil_first_cbh         [time]             {ceil.b1}  
        2  ceil_laser_temperature         [time]             {ceil.b1}  
        3         met_temperature         [time]              {met.b1}  
        4       twrmr_temperature         [time]  {sirs.b1, 1twrmr.c1}  
        """
        df = self._get_process_info_ret_field()
        return df[["group", "shape", "out_ds", "out_var", "name", "dims", "in_ds"]]

    def get_valid_transform_mappings(self, display_like_str: bool=False):
        """
        return available input_datastream--coordinate pairs for transformation.
        display_like in ["tuple", "str", "string"]
        
        EXAMPLE:
        get_valid_transform_mappings()
        >>
        [('ceil.b1', 'half_min_grid'), ('ceil.b1', 'mapped'),
        ('ceil.b1', 'half_min_grid'), ('met.b1', 'half_min_grid'),
        ('sirs.b1', 'mapped'), ('1twrmr.c1', 'mapped')]

        EXAMPLE:
        get_valid_transform_mappings(display_like="str")
        >>        
        ['ceil.b1+=>half_min_grid', 'ceil.b1+=>mapped',
        'ceil.b1+=>half_min_grid', 'met.b1+=>half_min_grid',
        'sirs.b1+=>mapped', '1twrmr.c1+=>mapped']
        """
        df = self.get_pcm_info_as_table()
        df_in_coord_pairs = df[["in_ds", "shape"]].explode("in_ds").drop_duplicates().reset_index(drop=True)
        if display_like_str:
            return (df_in_coord_pairs["in_ds"] + "+=>" + df_in_coord_pairs["shape"]).values.tolist()
        else:
            return df_in_coord_pairs.apply(lambda x: (x["in_ds"], x["shape"]), axis=1).values.tolist()

    def get_transform_pairs(self, display_like_str: bool=False):
        """
        Get a list of transformation pairs

        Note: since transformation is expensive, we ask the user to set transformation pairs manually

        EXAMPLE:

        """
        if not self._transform_pairs:
            return []
        if display_like_str:
            return [(ds_name + " +=> " + coord) for (ds_name, coord) in self._transform_pairs]
        else:
            return self._transform_pairs

    def set_transform_pair(self, input_datastream: str, coordinate: str):
        """
        Set transform pair (one pair at a time)
        Note: use clear_transform_pairs to delete. Doesn't support target delete at the moment.
        """
        # TODO: check if should log this. use print for now
        # TODO: at 3 test scenario for the following three cases.
        trans_pair = (input_datastream, coordinate)
        if trans_pair not in self.get_valid_transform_mappings():
            print(f"Transformation_pair: {trans_pair} is not a valid transformation pairs in {self.get_valid_transform_mappings()}.")
            print("Cannot set transform pair")        
        elif trans_pair in self._transform_pairs:
            print(f"Transformation_pair: {trans_pair} already exists in {self._transform_pairs}.")
            print("No transform pair added.")            
        else:
            self._transform_pairs.append(trans_pair)
            print(f"Added transformation_pair: {trans_pair} to the list.")
            print(f"Current Tansformation_pair: {self._transform_pairs}.")

        



    def clear_transform_pairs(self):
        """
        Clear out all the transform paris. Note: Doesn't support target delete at the moment.
        """
        self._transform_pairs = []

        
    
    def _group_2_dsname(self, group_name: str) -> str:
        """
        Helper function to map group name in pcm to datastream name, e.g., ceil_b1 -> ceil.b1
        """
        queries = self.process_info['ret']['queries']
        group_2_dsname: dict = {}
        for group, rules in queries.items():
            for rule in rules:
                datastream_name = f"{rule['class']}.{rule['level']}"
                if group_2_dsname.get(group):
                    if datastream_name not in group_2_dsname.get(group):  # keep unique
                        group_2_dsname[group].append(datastream_name)
                else:
                    group_2_dsname[group] = [datastream_name]
        return group_2_dsname[group_name]
    
    def _get_process_info_ret_field_raw(self) -> pd.DataFrame:
        """
        Helper function to get tablular formatted data of the process_info["ret"]["fields"]
        """
        json_field = self.process_info["ret"]["fields"]
        return pd.DataFrame(json_field)

    def _get_process_info_ret_field(self) -> pd.DataFrame:
        """
        Helper function to get processed tablular formatted data of the process_info["ret"]["fields"]
        """
        ds = self._get_process_info_ret_field_raw()
        df_fields_2 = ds.copy()
        df_fields_2["out_str"] = df_fields_2.out.apply(lambda x: str(x)) 
        df_fields_2["out_dict"] = df_fields_2.out.apply(lambda x: x[0] if x else {})
        df_fields_2["out_ds"] = df_fields_2["out_dict"].apply(lambda x: x.get("d") if x else "")
        df_fields_2["out_var"] = df_fields_2["out_dict"].apply(lambda x: x.get("f") if x else "")
        df_fields_2["in_ds"] = df_fields_2["group"].apply(lambda x: self._group_2_dsname(x))

        return df_fields_2
        
    def get_transform_plan(self) -> pd.DataFrame:
        """
        Get information about the transformation plan based on
        its associated input_datastream, coordiates/shape, and output_datasream

        EXAMPLE: 
                   in_ds          shape             out_ds                                       out_var  
            0  1twrmr.c1         mapped   adimappedgrid.c1                           [twrmr_temperature] 
            1    ceil.b1  half_min_grid  adiregulargrid.c1    [ceil_backscatter, ceil_laser_temperature] 
            2    ceil.b1         mapped                                                               [] 
            3     met.b1  half_min_grid  adiregulargrid.c1                             [met_temperature] 
        """
        df = self._get_process_info_ret_field()
        df_copy = df.copy()
        return df_copy.groupby(["in_ds", "shape", "out_ds"])["out_var"].apply(lambda x: list(x)).reset_index()

    # def _get_all_transformation_pairs(self) -> dict:
    #     """
    #     Helper function to get all the transformed pairs defined by PCM, 
    #     i.e., datastream names and the coordinate system that apply transformation accordingly

    #     EXAMPLE:
    #     {'1twrmr.c1--mapped': ('1twrmr.c1', 'mapped'),
    #     'ceil.b1--half_min_grid': ('ceil.b1', 'half_min_grid'),
    #     'ceil.b1--mapped': ('ceil.b1', 'mapped'),
    #     'met.b1--half_min_grid': ('met.b1', 'half_min_grid')}
    #     """
    #     df = self.get_transform_plan()
    #     transform_pair: dict = {}
    #     for plan in df[["in_ds", "shape"]].values:
    #         ds_name = plan[0]
    #         corrd = plan[1]
    #         transform_pair[ds_name + "--" + corrd] = tuple(plan)
    #     return transform_pair


    @property
    def adi_env_vars(self):
        return self._adi_env_vars

    def __repr__(self):
        return self.__module__ + "." +\
              self.__class__.__name__ + "(" + json.dumps(self.get_pcm_info(), indent=4)+ ")"

    @property
    def ds_ins_full_path(self):
        ds_ins_pickle_name = f"ds_ins_{self._pcm_name}_{self._site}_{self._facility}_{self._begin_date}_{self._end_date}.pickle"
        return os.path.join(self.pickle_path, ds_ins_pickle_name)     

    @property
    def ds_transforms_full_path(self):
        ds_transforms_pickle_name = f"ds_transforms_{self._pcm_name}_{self._site}_{self._facility}_{self._begin_date}_{self._end_date}.pickle"
        return os.path.join(self.pickle_path, ds_transforms_pickle_name)   
    
    @property
    def ds_outs_full_path(self):
        ds_outs_pickle_name = f"ds_outs_{self._pcm_name}_{self._site}_{self._facility}_{self._begin_date}_{self._end_date}.pickle"
        return os.path.join(self.pickle_path, ds_outs_pickle_name)     

    def set_datasteam_str_flag(self, ds_name: str, ds_str_flag: str):
        """
        Wrapper on adi_py.process def set_datastream_flags(dsid: int, flags: int)

        The original allowed flags are
        identified below:

        - dsproc.DS_STANDARD_QC     = Apply standard QC before storing a dataset.
    
        - dsproc.DS_FILTER_NANS     = Replace NaN and Inf values with missing values
                                      before storing a dataset.
    
        - dsproc.DS_OVERLAP_CHECK   = Check for overlap with previously processed data.
                                      This flag will be ignored and the overlap check
                                      will be skipped if reprocessing mode is enabled,
                                      or asynchronous processing mode is enabled.
    
        - dsproc.DS_PRESERVE_OBS    = Preserve distinct observations when retrieving
                                      data. Only observations that start within the
                                      current processing interval will be read in.
    
        - dsproc.DS_DISABLE_MERGE   = Do not merge multiple observations in retrieved
                                      data. Only data for the current processing interval
                                      will be read in.
    
        - dsproc.DS_SKIP_TRANSFORM  = Skip the transformation logic for all variables
                                      in this datastream.
    
        - dsproc.DS_ROLLUP_TRANS_QC = Consolidate the transformation QC bits for all
                                      variables when mapped to the output datasets.
    
        - dsproc.DS_SCAN_MODE       = Enable scan mode for datastream that are not
                                      expected to be continuous. This prevents warning
                                      messages from being generated when data is not
                                      found within a processing interval. Instead, a
                                      message will be written to the log file indicating
                                      that the procesing interval was skipped.
    
        - dsproc.DS_OBS_LOOP        = Loop over observations instead of time intervals.
                                      This also sets the DS_PRESERVE_OBS flag.
    
        - dsproc.DS_FILTER_VERSIONED_FILES = Check for files with .v# version extensions
                                             and filter out lower versioned files. Files
                                             without a version extension take precedence.

        """
        # TODO: make this method more user-friedly and pythonic and flexible (e.g., )
        # mechanism: set datastream-flag pair one at a time, and store at a dict-like self.ds_flags attribute,
        # then have the init_process_hook read through self.ds_flags then call the original def set_datastream_flags(dsid: int, flags: int)
        # note: def set_datastream_flags(dsid: int, flags: int) should be "private"

        # TODO: write value check for input. (i.e., ds_name, Q: can ds_name be output_datastream name?, flag)
        # TODO: discuss naming, note: even it is set one-at-a-time, it should not be called add_datastream_flag, since it can take out flag as well.

        if not self._ds_str_flags.get(ds_name):
            self._ds_str_flags[ds_name] = set([ds_str_flag]) # Note: make sure unique
        else:
            self._ds_str_flags[ds_name].add(ds_str_flag)

    def set_datasteam_int_flag(self, ds_name: str, ds_int_flag: int):
        """

        """
        # TODO: make this method more user-friedly and pythonic and flexible (e.g., )
        # mechanism: set datastream-flag pair one at a time, and store at a dict-like self.ds_flags attribute,
        # then have the init_process_hook read through self.ds_flags then call the original def set_datastream_flags(dsid: int, flags: int)
        # note: def set_datastream_flags(dsid: int, flags: int) should be "private"

        # TODO: write value check for input. (i.e., ds_name, Q: can ds_name be output_datastream name?, flag)
        

        if not self._ds_int_flags.get(ds_name):
            self._ds_int_flags[ds_name] = ds_int_flag
        else:
            self._ds_int_flags[ds_name] = self._ds_int_flags[ds_name] | ds_int_flag

    @property
    def ds_str_flags(self) -> Dict[str, int]:
        return self._ds_str_flags

    @property
    def ds_int_flags(self) -> Dict[str, int]:
        """
        TODO: basic idea: assume str_flags->int_flags, int_flags has higher presence. This logic needs to clean up.
        """
        # return dict() if no flag is set
        if not self._ds_str_flags and not self._ds_int_flags:  
            return self._ds_str_flags
        # first use self._ds_int_flags
        elif not self._ds_str_flags and self._ds_int_flags:  
            return self._ds_int_flags
        # else transform from self._ds_str_flags, especially if self._ds_str_flags and not self._ds_int_flags
        def _combine_int_flags(first, second):
            # combined int values
            return first | second

        for ds_name,ds_str_flags in self._ds_str_flags.items():
            ds_str_flags_2_int = [self._get_int_flag(flag) for flag in ds_str_flags]
            self._ds_int_flags[ds_name] = reduce(_combine_int_flags, ds_str_flags_2_int)
        return self._ds_int_flags

    @staticmethod
    def _get_int_flag(str_flag):
        ds_flag_str_2_int = {
        "DS_OVERLAP_CHECK": dsproc.DS_OVERLAP_CHECK, # 1
        "DS_STANDARD_QC": dsproc.DS_STANDARD_QC,  # 2
        "DS_PRESERVE_OBS": dsproc.DS_PRESERVE_OBS, # 4
        "DS_FILTER_NANS": dsproc.DS_FILTER_NANS, # 8                      
        "DS_DISABLE_MERGE": dsproc.DS_DISABLE_MERGE, # 16
        "DS_SKIP_TRANSFORM": dsproc.DS_SKIP_TRANSFORM, # 32
        "DS_ROLLUP_TRANS_QC": dsproc.DS_ROLLUP_TRANS_QC, # 64
        "DS_SCAN_MODE": dsproc.DS_SCAN_MODE, # 128
        "DS_OBS_LOOP": dsproc.DS_OBS_LOOP, #256
        # "DS_FILTER_VERSIONED_FILES": dsproc.DS_FILTER_VERSIONED_FILES  module 'dsproc3' has no attribute 'DS_FILTER_VERSIONED_FILES'
        }
        return ds_flag_str_2_int[str_flag]

    def init_process_hook(self):        

        # TODO: make an API entry point for the custom DSPROC redefinition 
        # custom DSPROC redefinition
        # self.pblhtsonde_dsid = self.get_dsid(self.DS_IN_PBLHTSONDE1MCFARL_C1)        
        # if self.pblhtsonde_dsid is None:            # This will terminate the process and also log an error to the process log            
        #     raise Exception(f'Could not get input dsid for pblhtsonde1mcfarl.c1 input datasource')        
        # dsproc.set_datastream_flags(self.pblhtsonde_dsid, dsproc.DS_OBS_LOOP)

        
        if self.ds_int_flags:
            for ds_name, ds_flag in self.ds_int_flags.items():
                ds_id: int = self.get_dsid(ds_name)      
                dsproc.set_datastream_flags(ds_id, ds_flag)
                
    # def init_process_hook(self):
    #     """-------------------------------------------------------------------------------------------------------------
    #     This hook will will be called once just before the main data processing loop begins and before the initial
    #     database connection is closed.
    #     -------------------------------------------------------------------------------------------------------------"""
        
    #     # Here is an example of setting obs-based processing, which is controlled by ADI flags.  (Delete this stubbed
    #     # out code if you do not need obs-based procesing.)

    #     # Get the ADI dsid for one of your input datastreams
    #     # dsid = self.get_dsid(self.DS_IN_CO2FLX25M_B1)

    #     # dsid will be None if the datastream does not exist in ADI
    #     # if dsid is None:
    #         # This will terminate the process and also log an error to the process log
    #         # raise Exception(f'Could not find input dsid for { self.DS_IN_CO2FLX25M_B1 }')

    #     # Set the obs loop control flag for that input datastream
    #     # self.set_datastream_flags(dsid, dsproc.DS_OBS_LOOP)
        

    def pre_transform_hook(self, begin_date: int, end_date: int):
        """-------------------------------------------------------------------------------------------------------------
        This hook will be called once per processing interval just prior to data transformation,and after the retrieved
        observations are merged and QC is applied.

        Args:
            begin_date (int): the begin time of the current processing interval
            end_date (int): the end time of the current processing interval
        -------------------------------------------------------------------------------------------------------------"""
        
        # First get any retrieved datasets that we need to modify (as an XArray dataset).
        # (Note that you can get the dataset by datastream_name/site/facility by calling self.get_retrieved_dataset(),
        # OR you can get the dataset by dsid (see init_process_hook example above) by calling
        # self.get_retrieved_dataset_by_dsid())
        # ds = self.get_retrieved_dataset(self.DS_IN_CO2FLX25M_B1)

        # Automatically get all the PCM-defined input datasets
        # TODO: need to handle get_retrieved_dataset vs. get_retrieved_datasets
        # TODO: need to handle observed dataset cannot be retrieved without setting set_datastream_flags
        ds_ins_per_run: dict = {}  # all the input datastreams per process run
        for ds_in_name in self.ds_in_names:
            # TODO: verify the retrive rules, i.e., to make it more general/flexible, should we use get_retrieved_dataset or get_retrieved_datasets
            ds = self.get_retrieved_dataset(ds_in_name)  
            # ds_ins_per_run[ds_in_name] = ds
            if ds:
                ds_copy = ds.copy()  # note: it is important to have a deep-copy of it
            else:
                ds_copy = ds
            ds_ins_per_run[ds_in_name] = ds_copy
        self._ds_ins.append(ds_ins_per_run)

        # Dataset will be None if the datastream does not exist in ADI
        # if ds is None:
        #     # This will terminate the process and also log an error to the process log.  Only do this if this particular
        #     # datastream is required
        #     raise Exception(f'Could not find input datastream for { self.DS_IN_CO2FLX25M_B1 }')

        #     # As an alternative, you can throw SkipProcessingIntervalException to skip to the next processing interval
        #     # You can decide if this skip should be logged as a warning or an info to the log
        #     # ADILogger.info(f'Skipping processing interval because { self.DS_IN_CO2FLX25M_B1 } not found.')
        #     # raise SkipProcessingIntervalException(f'Could not find input datastream for { self.DS_IN_CO2FLX25M_B1 }')

        # Perform your work here...

        # Now you need to push any changes you made back to ADI
        # self.sync_datasets(ds)
        

        # This is an example of adding a level 3 debug log via ADILogger (levels 1-4 are supported)
        ADILogger.debug("This is a micro debug statement, often used for printing values of variables.", 3)
        ADILogger.debug("I don't need to debug when hooks start and stop because this is done for me by the parent class!!", 3)

    def post_transform_hook(self, begin_date: int, end_date: int):
        """-------------------------------------------------------------------------------------------------------------
        This hook will be called once per processing interval just after data transformation, but before the output
        datasets are created.

        Args:
          begin_date (int): the begin time of the current processing interval
          end_date (int):   the end time of the current processing interval
        -------------------------------------------------------------------------------------------------------------"""
        
       
        # ds_tranforms_per_run: dict = {}  # all the input datastreams per process run
        # for ds_in_name in self.ds_in_names:
        #     ds_tranforms_per_run[ds_in_name] = self.get_transformed_dataset(ds_in_name, self.ds_coord_names[0])
        # self.ds_transforms.append(ds_tranforms_per_run)

        # TODO: perform full cross paired transform is very expensive, consider use deafult transform method,
        # transform how: all (all the paire), None (no transform), customer specified

        ds_transforms_per_run: dict = {}  # all the input datastreams per process run
        if not self._transform_pairs:
            # raise SkipProcessingIntervalException("Skip post_transform_hook")
            return
        for pair in self._transform_pairs:
            ds = self.get_transformed_dataset(pair[0], pair[1])  # TODO: handle edge case of get_transformed_datasets later
            if ds:
                ds_copy = ds.copy()  # note: it is important to have a deep-copy of it
            else:
                ds_copy = ds     
            plan_name = pair[0] + "+=>" + pair[1]
            ds_transforms_per_run[plan_name] = ds_copy
        self._ds_transforms.append(ds_transforms_per_run)

        # This is an example of adding a level 3 debug log via ADILogger (levels 1-4 are supported)
        ADILogger.debug("This is a micro debug statement, often used for printing values of variables.", 3)
        ADILogger.debug("I don't need to debug when hooks start and stop because this is done for me by the parent class!!", 3)

    def process_data_hook(self, begin_date: int, end_date: int):
        """-------------------------------------------------------------------------------------------------------------
        This hook will be called once per processing interval just after the output datasets are created, but before
        they are stored to disk.

        Args:
            begin_date (int): the begin time of the current processing interval
            end_date (int):   the end time of the current processing interval
        -------------------------------------------------------------------------------------------------------------"""
        
        # First get any output datasets that we need to modify (as an XArray dataset)
        # (Note that you can get the dataset by datastream_name by calling self.get_output_dataset(),
        # OR you can get the dataset by dsid (see init_process_hook example above) by calling
        # self.get_output_dataset_by_dsid())
        # ds = self.get_output_dataset(self.DS_OUT_KMPBLHTDLRF_C1)

        # Automatically get all the PCM-defined input datasets
        ds_outs_per_run: dict = {}  # all the input datastreams per process run
        for ds_out_name in self.ds_out_names:
            ds = self.get_output_dataset(ds_out_name)
            # self.sync_datasets(ds)
            # ds_outs_per_run[ds_out_name] = ds
            if ds:
                ds_copy = copy.deepcopy(ds)  # note: it is important to have a deep-copy of it
            else:
                ds_copy = ds
            ds_outs_per_run[ds_out_name] = ds_copy
        self._ds_outs.append(ds_outs_per_run)

        # Dataset will be None if the datastream does not exist in ADI
        
        # if ds is None:
        #     # This will terminate the process and also log an error to the process log.  Only do this if this particular
        #     # datastream is required
        #     raise Exception(f'Could not find output datastream for { self.DS_OUT_KMPBLHTDLRF_C1 }')

        #     # As an alternative, you can throw SkipProcessingIntervalException to skip to the next processing interval
        #     # You can decide if this skip should be logged as a warning or an info to the log
        #     # ADILogger.info(f'Skipping processing interval because { self.DS_OUT_KMPBLHTDLRF_C1 } not found.')
        #     # raise SkipProcessingIntervalException(f'Could not find output datastream for { self.DS_OUT_KMPBLHTDLRF_C1 }')
        
        # Perform your work here...

        # Now you need to push any changes you made back to ADI
        # self.sync_datasets(ds)
        

        # This is an example of adding a level 3 debug log via ADILogger (levels 1-4 are supported) (levels 1-4 are supported)
        ADILogger.debug("This is a micro debug statement, often used for printing values of variables.", 3)
        ADILogger.debug("I don't need to debug when hooks start and stop because this is done for me by the parent class!!", 3)
        
    def finish_process_hook(self):
        """-----------------------------------------------------------------------
        This hook will be called once just after the main data processing loop finishes.  This function should be used
        to clean up any temporary files used.

        -----------------------------------------------------------------------"""
        pass

        # Note: this hook is not per process-vise, but after all the process inverals are finished.
        # self.ds_ins
        # self.ds_outs
        self._save_ds()    
    

    def quicklook_hook(self, begin_date: int, end_date: int):
        """-------------------------------------------------------------------------------------------------------------
        This hook will be called once per processing interval just after all data is stored.

        Args:
            begin_date (int): the begin timestamp of the current processing interval
            end_date (int): the end timestamp of the current processing interval
        -------------------------------------------------------------------------------------------------------------"""
        # see adi_example1_py_newapi for an example implementation
        pass

    def run(self):
        """overide the parent method to prevent calling it directly."""
        print("Warning. This method should not be called, especially from a Notebook environment")

    def _run(self) -> int:
        """-----------------------------------------------------------------------
        mimic the parent class def run method
        Returns:
            int: The processing status:

            - 1 if an error occurred
            - 0 if successful
        -----------------------------------------------------------------------"""

        dsproc.use_nc_extension()

        # TODO: make sure that ADI doesn't care if we set a hook if it's not
        # used for the given processing model
        dsproc.set_init_process_hook(self._internal_init_process_hook)
        dsproc.set_pre_retrieval_hook(self._internal_pre_retrieval_hook)
        dsproc.set_post_retrieval_hook(self._internal_post_retrieval_hook)
        dsproc.set_pre_transform_hook(self._internal_pre_transform_hook)
        dsproc.set_post_transform_hook(self._internal_post_transform_hook)
        dsproc.set_process_data_hook(self._internal_process_data_hook)
        dsproc.set_finish_process_hook(self._internal_finish_process_hook)
        dsproc.set_quicklook_hook(self._internal_quicklook_hook)

        # site, facility, begin_date, end_date
        # TODO: make -D, -R, --dynamic-dods as parameter
        this_file_path = "xx" # not important
        sys_args = [this_file_path, 
                    '-n', 'pblhtdlrf_training_validation', 
                    '-s', self._site, 
                    '-f', self._facility, 
                    '-b', self._begin_date, '-e', self._end_date, 
                    '-D', '2', 
                    '-R', 
                    '--dynamic-dods']
        
        exit_value = dsproc.main(
            # sys.argv,
            sys_args,
            self.process_model,
            self.process_version,
            self.process_names)      
        return exit_value

    def _save_ds(self):
        """
        Persist self.ds_ins and self.ds_outs based as pickle on certain naming convention
        """
        # mkdir to pickle path
        self._mkdir(self.pickle_path)
        # save ds_ins as pickle
        self._pickle_dump_ds(self.ds_ins_full_path, self._ds_ins)
        # save ds_trnasforms as pickle
        self._pickle_dump_ds(self.ds_transforms_full_path, self._ds_transforms) 
        # save ds_outs as pickle
        self._pickle_dump_ds(self.ds_outs_full_path, self._ds_outs)

    @staticmethod
    def _mkdir(path: pathlib.Path) -> bool:
        """
        Helper function to make dir, if exists skip. 
        Return True if sucess."""
        try:
            path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def _pickle_dump_ds(abs_file, var):
        """
        TODO: this method needs to clean up. And bug exists."""
        # try:
        #     if not os.path.isfile(abs_file):
        #         f = open(abs_file, "x")
        #         f.close()
        #     # with open(abs_file, 'ab+') as f:
        #     #     pickle.dump(var, f)               
        #     with open(abs_file, 'wb+') as f:
        #         pickle.dump(var, f)               
        # except Exception as e:
        #     print(e)
        #     # Don't skep silently
        #     raise e
        with open(abs_file, 'wb+') as f:
                pickle.dump(var, f)            

    @staticmethod
    def _pickle_load_ds(abs_file):
        try:
            with open(abs_file, 'rb+') as f:
                var = pickle.load(f)             
            return var  
        except Exception as e:
            print(e)
            # Don't skep silently
            raise e
    
    @staticmethod
    def retrieve_process(proc_name):
        """
        Mimic create_adi
        ...

        Retrieve a JSON file from the DSDB with all the information specified by the processes 
        definition

        @param process: 
            The specified process to retrieve the JSON data of
        # @param local_input_file: 
        #     The name of the JSON file to use as the input instead of the DSDB

        # @return process: 
        #     Deserialized JSON data of the requested process
        """

        # if local_input_file is None:

        #     # Get the input JSON file since it isn't specified
        #     json_request = requests.get("https://{}?action=proc-dump&templater=1&name={}&type=VAP"\
        #                                 .format(DATABASE_URL, process_name))
        #     process = json_request.json()
        #     category = process['category']
            
        #     if category is None:
        #         sys.stdout.write("ERROR: PCM process could not be found.\n")
        #         sys.exit(1)    

        #     if category == "Instrument": # Ingest
        #         json_request2 = requests.get("https://{}?action=proc-dump&templater=1&name={}&type=Ingest"\
        #                                     .format(DATABASE_URL, process_name))
        #         process = json_request2.json()
        # else:
        #     json_file = open(local_input_file, 'r')
        #     process = json.load(json_file)
        #     json_file.close()

        # if dump_json: # Print the process JSON object instead of writing it somewhere
        #     print(json.dumps(process, indent=4))
        #     return

        # Get the input JSON file since it isn't specified
        DATABASE_URL = "engineering.arm.gov/dsdb/cgi-bin/procdb"
        json_request = requests.get("https://{}?action=proc-dump&templater=1&name={}&type=VAP"\
                                    .format(DATABASE_URL, proc_name))
        process = json_request.json()
        category = process['category']
        
        if category is None:
            sys.stdout.write("ERROR: PCM process could not be found.\n")
            sys.exit(1)    

        if category == "Instrument": # Ingest
            json_request2 = requests.get("https://{}?action=proc-dump&templater=1&name={}&type=Ingest"\
                                        .format(DATABASE_URL, proc_name))
            process = json_request2.json()

        return process

    @staticmethod
    def get_input_datastreams(process):
        input_datastreams = set()
        try:
            queries = process['ret']['queries']
            for dataset_name, rules in queries.items():
                for rule in rules:
                    datastream_name = f"{rule['class']}.{rule['level']}"
                    input_datastreams.add(datastream_name)
        except KeyError:
            pass

        return sorted(list(input_datastreams))

    @staticmethod
    def get_output_datastreams(process):

        output_datastreams = set()
        try:
            outputs = process['outputs']
            for output in outputs:

                if type(output) == str:
                    output_datastreams.add(output)

                else:
                    # Sadly, I can't understand this data structure, so I call it 'blob'
                    for blob in output:
                        datastream_name = f"{blob['class']}.{blob['level']}"
                        output_datastreams.add(datastream_name)
        except KeyError:
            pass

        return sorted(list(output_datastreams))

    @staticmethod
    def get_coordinate_systems(process):
        coordinate_systems = []
        try:
            shapes = process['ret']['shapes']
            for shape in shapes:
                coordinate_systems.append(shape)
        except KeyError:
            pass

        return sorted(coordinate_systems)

    def process(self, cached=False):
        """
        A wrapper on self.run(), but calling from subprocess
        # TODO: try to return the exit value from _run() and feed to process()
        # TODO: explore with the idea to use dummy class rather than subprocess to invoke the async process.
        #  (maybe it is cleaner. e.g., --set_datastream_flags is too recursive)
        """

        # if cached==True and pickle dump files exist, then skip 
        if cached and os.path.isfile(self.ds_ins_full_path) and os.path.isfile(self.ds_outs_full_path) and os.path.isfile(self.ds_transforms_full_path):
            return
            
        # TODO: currently use `python <script_name>` style, consider to encapsulate into package in the future
        this_file_path = os.path.dirname(__file__)
        this_file_name = os.path.basename(__file__)
        this_file_absolute_path = os.path.join(this_file_path, this_file_name)
        command = f"python {this_file_absolute_path} " +\
                    f"-n {self._pcm_name} " +\
                    f"-s {self._site} " +\
                    f"-f {self._facility} " +\
                    f"-b {self._begin_date} " +\
                    f"-e {self._end_date} "
        command_split = command.split()  
        # feed in datastream_flag info
        if self.ds_int_flags:
            # command_pair = '"'
            command_pair = ''
            for ds_name, int_flag in self.ds_int_flags.items():
                command_pair = command_pair + ds_name+ " " 
                command_pair = command_pair+ str(int_flag) + " " 
            # command_pair = command_pair + '"'
            command_split += ["--set_datastream_flags"]
            command_split += [command_pair]
        # feed in transformation_pair info
        if self._transform_pairs:
            command_pair = ''
            for ds_name, coord_name in self._transform_pairs:
                command_pair = command_pair + ds_name+ " " 
                command_pair = command_pair+ coord_name + " " 
            command_split += ["--set_transform_pairs"]
            command_split += [command_pair]

        # feed in env-vars
        my_env = os.environ.copy()
        my_env["testing_env_var"] = "tesing-env-var"  # testing
        
        # Note: use subprocess.run to wait for the whole process to end, 
        # adi output should print out on the terminal
        # print("=============================")
        # print("=============================")
        # print(command_split)
        # print("=============================")
        # print("=============================")
        subprocess.run(command_split, env=my_env) 

    def dry_run(pcm_name, site, facility):
        """
        TODO: method to check if the the process is valid with the associated parameters 
        """
        pass

    def get_ds_ins(self):
        """
        Get persisted ds_ins variables
        """
        if not os.path.isfile(self.ds_ins_full_path):
            raise Exception(f"{self.ds_ins_full_path} NOT exist. Run process() first.")
        # return self._pickle_load_ds(self.ds_ins_full_path)
        return AdiDatasetList(self._pickle_load_ds(self.ds_ins_full_path))

    def get_ds_transforms(self):
        """
        Get persisted ds_transform variables
        """
        if not os.path.isfile(self.ds_transforms_full_path):  
            raise Exception(f"{self.ds_transforms_full_path} NOT exist. Run process() first.") 
        # return self._pickle_load_ds(self.ds_transforms_full_path)
        return AdiDatasetList(self._pickle_load_ds(self.ds_transforms_full_path))

    def get_ds_outs(self):
        """
        Get persisted ds_outs variables
        """
        if not os.path.isfile(self.ds_outs_full_path):
            raise Exception(f"{self.ds_outs_full_path} NOT exist. Run process() first.")
        # return self._pickle_load_ds(self.ds_outs_full_path)
        return AdiDatasetList(self._pickle_load_ds(self.ds_outs_full_path))

    def  _get_retrieved_dataset(self):
        pass
        # TODO: just like run, get_retrieved_dataset cannot be called outside the run process/from init_hook to finish_hook, 
        # otherwise the cbind part will complain. (connection issue?) 
        # use a run_on_flag to control whether such methods can be called. 
        # (basically, it is method like dsproc.get_retrieved_dataset() causes the problem)

    def config_adi_env_vars(self, 
                            DATASTREAM_DATA_IN="/data/archive",
                            DATASTREAM_DATA_OUT="default",
                            QUICKLOOK_DATA="default",
                            LOGS_DATA="default",
                            CONF_DATA="default",
                            ADI_PY_MODE="development",
                            **kwargs
                        ):
        """
        TODO: develop validation check, e.g., figure out available options for ADI_PY_MODE
        TODO: discuss if use "default" or None for signature deafult value
        """
        
        if DATASTREAM_DATA_OUT == "default":
            DATASTREAM_DATA_OUT = os.path.join(self.ADI_DATA_DIR, "datastream/")
        if QUICKLOOK_DATA == "default":
            QUICKLOOK_DATA = os.path.join(self.ADI_DATA_DIR, "quicklook/")
        if LOGS_DATA == "default":
            LOGS_DATA = os.path.join(self.ADI_DATA_DIR, "logs/")
        if CONF_DATA == "default":
            CONF_DATA = os.path.join(self.ADI_DATA_DIR, "conf/")

        adi_env_var_old = self._adi_env_vars.copy()

        self._adi_env_vars = {
            "DATASTREAM_DATA_IN": DATASTREAM_DATA_IN,
            "DATASTREAM_DATA_OUT": DATASTREAM_DATA_OUT,
            "QUICKLOOK_DATA": QUICKLOOK_DATA,
            "LOGS_DATA": LOGS_DATA,
            "CONF_DATA": CONF_DATA,
            "ADI_PY_MODE": ADI_PY_MODE
        }

        for k, v in self._adi_env_vars.items():
            os.environ[k] = str(v)

        diff_adi_env_vars = { k : self._adi_env_vars[k] for k in self._adi_env_vars.keys() 
                             if self._adi_env_vars[k] != adi_env_var_old }
        
        if adi_env_var_old:  # only print after the initialization
            print(f"Updated adi_env_vars to {diff_adi_env_vars}")
        return self._adi_env_vars







def get_arg():
    # Initialize parser
    parser = argparse.ArgumentParser(
        prog="adi_proc",
        description="A standalone adi_process program",
        # epilog="Thanks for using %(prog)s! :)",
    )

    # Adding optional argument
    parser.add_argument("-n", "--name", action="store", default="gcp", type=str, required=True,
                        metavar="<NAME>",
                        help="name of PCM process, e.g., adi_demo_0")
    parser.add_argument("-s", "--site", action="store", default="gcp", type=str, required=True,
                        metavar="<SITE>",
                        help="site, e.g., gcp")
    parser.add_argument("-f", "--facility", action="store", default="c1", type=str, required=True,
                        metavar="<FACILITY>",
                        help="facility, e.g., c1")
    parser.add_argument("-b", "--begin_date", action="store", type=str, required=True,
                        metavar="<BEGIN_DATE>",
                        help="begin date, e.g., 20100101")
    parser.add_argument("-e", "--end_date", action="store", type=str, required=True,
                        metavar="<END_DATE>",
                        help="end date, e.g., 20100102")
    parser.add_argument("--set_datastream_flags", action="store", type=str,
                        metavar="<list of datastream-flag pairs>",
                        help="list of datastream-flag pairs, seperate with space, e.g., ds-name-1 10 ds-namee-2 8 ")
    parser.add_argument("--set_transform_pairs", action="store", type=str,
                        metavar="<list of datastream-coordinate pairs for transformation>",
                        help="list of datastream-coordinate pairs for transformation, seperate with space, e.g., met.b1 half_min_grid sirs.b1 mapped")

    args = parser.parse_args()

    return args

def pairwise(iterable):
    """ use to organize ds_name ds_flag pair on command line
    (s0, s1, s2, s3, s4, s5) -> (s0, s1), (s2, s3), (s4, s5), ...
    """
    a = iter(iterable)
    return zip(a, a)


def main():
    """
    Note: This method not only serve as entry point when calling script from command line,
    but also a sudo-async process to run adi-hooks from a notebook.
    """
    # sys.exit(PblhtdlrfTrainingValidation().run())
    

    # pbl_proc = PblhtdlrfTrainingValidation(pcm_name="adi_demo_0", site="sgp", facility="C1", begin_date="20190219", end_date="20190220")
    args = get_arg()

    # initialize instance using parameters from command line
    adi_process = ADI_Process(
        pcm_name=args.name,
        site=args.site,
        facility=args.facility,
        begin_date=args.begin_date,
        end_date=args.end_date
    )

    # set environment variable


    # set flags
    flag_command = args.set_datastream_flags  # e.g., 'pblhtsonde1mcfarl.c1 258 pblhtsonde1mcfarl.c1xx 2 '
    if flag_command:
        for ds_name, int_flag in pairwise(flag_command.split()):
            adi_process.set_datasteam_int_flag(ds_name, int(int_flag))

    # set transformation pairs
    transform_pair_command = args.set_transform_pairs
    if transform_pair_command:
        for ds_name, coord in pairwise(transform_pair_command.split()):
            adi_process.set_transform_pair(ds_name, coord)

    adi_process._run()


if __name__ == '__main__':

    main()
