import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from adi_notebook.adi_runner import ADI_Process, AdiDatasetDict, AdiRunner
import sys
# import dsproc3 as dsproc
import pickle


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

    prc_adi_demo_0 = AdiRunner(pcm_name="adi_demo_0", site="sgp", facility="C1", 
                           begin_date="20190119", end_date="20190120")  
    print(prc_adi_demo_0)    
    # print(prc_adi_demo_0.get_valid_transform_mappings())
    # print(prc_adi_demo_0.get_transform_pairs())
    # # prc_adi_demo_0.set_transform_pair("ceil.b1", "dfd")
    # # prc_adi_demo_0.set_transform_pair("ceil.b1", "half_min_grid")
    # prc_adi_demo_0.set_transform_pair('met.b1', 'half_min_grid')
    # # pbl_proc.process(cached=False)
    # ds_ins = prc_adi_demo_0.get_ds_ins()
    prc_adi_demo_0.set_transform_pair('met.b1', 'half_min_grid')
    prc_adi_demo_0.process()
    ds_ins = prc_adi_demo_0.input_datasets
    print(ds_ins[0]["met.b1"])
    print(ds_ins)
    print(ds_ins[0])
    # # ds_outs = pbl_proc.get_ds_outs()
    # print(prc_adi_demo_0.get_transform_pairs())
    # prc_adi_demo_0.process()
    # print(prc_adi_demo_0.get_ds_transforms())
    # print(prc_adi_demo_0.get_ds_ins())

    x = 1

if __name__ == '__main__':
    main()