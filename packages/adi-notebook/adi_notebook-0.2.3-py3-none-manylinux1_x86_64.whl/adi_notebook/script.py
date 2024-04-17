import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from adi_notebook.adi_proc import ADI_Process, AdiDatasetDict
import sys
# import dsproc3 as dsproc
import pickle
import uuid
from adi_py import Process, ADILogger

# def pre_transformed_hook():
#         """
#         TODO: note: the function needs to be defined at global scope, 
#             other wise will cause pickle error: AttributeError: Can't pickle local object
            
#         TOD: find other solution that relax the constraints to define at global scope   """
            
#         print("!!!!!!!!!!!!!!!!!!!!!!!!")
#         print("I am pre_transformed_hook")
#         print("!!!!!!!!!!!!!!!!!!!!!!!!")


def inject_pre_transform_hook(ds_met_b1):
        """
        TODO: note: the function needs to be defined at global scope, 
            other wise will cause pickle error: AttributeError: Can't pickle local object
            
        TOD: find other solution that relax the constraints to define at global scope   """
            
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("I am inject_pre_transform_hook")
        ds_met_b1["met_temperature"].data = ds_met_b1["met_temperature"].data * 2
        print("!!!!!!!!!!!!!!!!!!!!!!!!")


def main_custom_adi_hooks_workflow():
    pass

    def inject_pre_transform_hook_2(ds_met_b1):
        """
        TODO: note: the function needs to be defined at global scope, 
            other wise will cause pickle error: AttributeError: Can't pickle local object
            
        TOD: find other solution that relax the constraints to define at global scope   """
            
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("I am inject_pre_transform_hook")
        print(f'before ds_met_b1["met_temperature"].data {ds_met_b1["met_temperature"].data[0]}')
        ds_met_b1["met_temperature"].data = ds_met_b1["met_temperature"].data * 2
        print(f'after ds_met_b1["met_temperature"].data {ds_met_b1["met_temperature"].data[0]}')
        print("!!!!!!!!!!!!!!!!!!!!!!!!")

    
    adi_proc = ADI_Process(pcm_name="adi_demo_0", site="sgp", facility="C1", 
                           begin_date="20190119", end_date="20190120")
    
    # # _save_custom_hooks
    
    # adi_proc._custom_adi_hooks = {"pre_transformed_hook": inject_pre_transform_hook}
    # adi_proc._save_custom_adi_hooks()

    # _load_custom_hooks
    custom_adi_hooks_loaded = adi_proc._load_custom_adi_hooks()
    print(custom_adi_hooks_loaded)

    # set_injected_pre_transform
    arg_mapping = {"ds_met_b1": "met.b1"}
    adi_proc.set_custom_adi_hooks("injected_pre_transform_hook", inject_pre_transform_hook_2, arg_mapping)
    
    # set package path for local import
    adi_proc.set_local_package_path(os.path.dirname(__name__))

    # process
    adi_proc.process()


    # double check
    custom_adi_hooks_loaded = adi_proc._load_custom_adi_hooks()
    print(custom_adi_hooks_loaded)



    x = 1

def main_dynamic_import_within_callback():

    def inject_pre_transform_hook_w_callback(ds_met_b1):
        """
        TODO: note: the function needs to be defined at global scope, 
            other wise will cause pickle error: AttributeError: Can't pickle local object
            
        TOD: find other solution that relax the constraints to define at global scope   """

        # uuid = __import__("uuid")
        import uuid
        package_path = "/home/kefeimo/project/adi-notebook/src/adi_notebook"  # TODO: encapsulate this part
        sys.path.append(package_path)
        # x_plus_one = __import__("custom_import.x_plus_one")
        # custom_import = __import__("custom_import")
        from custom_package import custom_import as custom_import 
            
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("I am inject_pre_transform_hook w/ callback")
        print(str(uuid.uuid1()))
        print(f"4 plus one is {custom_import.x_plus_one(4)}")
        print(f"4 times two is {custom_import.x_times_two(4)}")
        print(f'before ds_met_b1["met_temperature"].data {ds_met_b1["met_temperature"].data[0]}')
        ds_met_b1["met_temperature"].data = ds_met_b1["met_temperature"].data * 2
        print(f'after ds_met_b1["met_temperature"].data {ds_met_b1["met_temperature"].data[0]}')
        print("!!!!!!!!!!!!!!!!!!!!!!!!")

    
    adi_proc = ADI_Process(pcm_name="adi_demo_0", site="sgp", facility="C1", 
                           begin_date="20190119", end_date="20190120")
    
    # # _save_custom_hooks
    
    # adi_proc._custom_adi_hooks = {"pre_transformed_hook": inject_pre_transform_hook}
    # adi_proc._save_custom_adi_hooks()

    # _load_custom_hooks

    # set_injected_pre_transform
    arg_mapping = {"ds_met_b1": "met.b1"}
    adi_proc.set_custom_adi_hooks("injected_pre_transform_hook", inject_pre_transform_hook_w_callback, arg_mapping)
    
    # process
    adi_proc.process()

    x = 1
     

def main():

    pass
    # case 3
    # pbl_proc = ADI_Process(pcm_name="pblhtdlrf_training_validation", site="sgp", facility="C1", 
    #                        begin_date="20190119", end_date="20190120")
    # # pbl_proc.set_datasteam_str_flag("pblhtsonde1mcfarl.c1", "DS_OBS_LOOP")
    # # # not essential but to show the capability to set multiple stream flags
    # # pbl_proc.set_datasteam_str_flag("pblhtsonde1mcfarl.c1", "DS_STANDARD_QC")  

    # prc_adi_demo_4 = ADI_Process(pcm_name="adi_demo_4", site="sgp", facility="C1", 
    #                        begin_date="20190119", end_date="20190120") 
    # prc_adi_demo_4.process()
    # ds_ins = prc_adi_demo_4.get_ds_ins()
    # ds_outs = prc_adi_demo_4.get_ds_outs()

    # pbl_proc.set_datasteam_str_flag("pblhtsonde1mcfarl.c1xx", "DS_STANDARD_QC")
    # pbl_proc.run()
    # # ds = pbl_proc.get_retrieved_dataset(pbl_proc.DS_IN_CO2FLX25M_B1)
    # print("==================================ds_globe")
    # print(len(pbl_proc.ds_globe))
    # print(pbl_proc.ds_globe)

    prc_adi_demo_0 = ADI_Process(pcm_name="adi_demo_0", site="sgp", facility="C1", 
                           begin_date="20190119", end_date="20190120")  
    print(prc_adi_demo_0)    
    # print(prc_adi_demo_0.get_valid_transform_mappings())
    # print(prc_adi_demo_0.get_transform_pairs())
    # # prc_adi_demo_0.set_transform_pair("ceil.b1", "dfd")
    # # prc_adi_demo_0.set_transform_pair("ceil.b1", "half_min_grid")
    # prc_adi_demo_0.set_transform_pair('met.b1', 'half_min_grid')
    # # pbl_proc.process(cached=False)
    # ds_ins = prc_adi_demo_0.get_ds_ins()
    ds_ins = prc_adi_demo_0.input_datasets
    print(ds_ins[0]["met.b1"])
    # # ds_outs = pbl_proc.get_ds_outs()
    # print(prc_adi_demo_0.get_transform_pairs())
    # prc_adi_demo_0.process()
    # print(prc_adi_demo_0.get_ds_transforms())
    # print(prc_adi_demo_0.get_ds_ins())

    x = 1

if __name__ == '__main__':
    # main()
    # main_custom_adi_hooks_workflow()
    main_dynamic_import_within_callback()