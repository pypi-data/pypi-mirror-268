import os

import pandas as pd
from alpharaw.thermo import ThermoRawData
from alphabase.io.hdf import HDF_File
from pglyco.raw_data.sister_spec_merger import merge_sister_ms2
from pglyco.raw_data.raw_utils import get_activation_from_scan_event
from pglyco.raw_data.mgf_writer import df_to_mgf
from pglyco.raw_data.ms1ms2_writer import df_to_ms1_ms2_for_pParse

from pglyco.utils.logger import logging

def parse_one_raw(
    raw_path:str,
    merge_ppm_tol = 20.0,
    merge_scan_window = 10,
    keep_if_no_sisters = True,
):
    reader = load_thermo_raw(raw_path)
    hdf = HDF_File(raw_path+".hdf5", read_only=False)
    if hasattr(hdf.ms_data, "sister_map_df"):
        try:
            reader.merged_spec_df = hdf.ms_data.merged_spec_df.values
            reader.merged_peak_df = hdf.ms_data.merged_peak_df.values
            reader.sister_map_df  = hdf.ms_data.sister_map_df.values
            return reader
        except:
            pass

    spec_df, peak_df, sister_map_df = merge_sister_ms2(
        reader.spectrum_df, reader.peak_df,
        ppm_tol = merge_ppm_tol,
        sister_scan_window=merge_scan_window,
        keep_if_no_sisters=keep_if_no_sisters,
    )
    
    if len(spec_df) < len(reader.spectrum_df):
        logging.info(f"Merging {len(reader.spectrum_df)-len(spec_df)} sister scans")
        hdf.ms_data.merged_spec_df = spec_df
        hdf.ms_data.merged_peak_df = peak_df
        hdf.ms_data.sister_map_df = sister_map_df
        reader.merged_spec_df = spec_df
        reader.merged_peak_df = peak_df
        reader.sister_map_df = sister_map_df
    else:
        logging.info(f"No sister scans found, skip merging")
        reader.merged_spec_df = reader.spectrum_df
        reader.merged_peak_df = reader.peak_df
        reader.sister_map_df = None
    logging.info(f"Finish '{raw_path}.hdf5'")
    return reader

def convert_df(raw_path, reader, convert_to):
    if not os.path.isfile(raw_path+".redo"): 
        logging.info(f"Skip '{convert_to}' conversion")
        return
    logging.info(f"Converting '{raw_path}' to '{convert_to}' ...")
    if convert_to == "mgf":
        df_to_mgf(
            raw_path=raw_path,
            spectrum_df=reader.merged_spec_df,
            peak_df=reader.merged_peak_df,
        )
    elif convert_to == "ms1ms2":
        df_to_ms1_ms2_for_pParse(
            raw_path=raw_path,
            spectrum_df=reader.merged_spec_df,
            peak_df=reader.merged_peak_df
        )
    os.remove(raw_path+".redo")
    logging.info(f"Finish '{raw_path}' to '{convert_to}' ...")

def load_thermo_raw(raw_path:str):
    reader = ThermoRawData(
        process_count=1, dda=True,
        auxiliary_items=["scan_event_string"],
    )
    try:
        reader.load_hdf(raw_path+".hdf5")
        logging.info(f"Skip '{raw_path}.hdf5' as it exists")
        return reader
    except:
        pass

    logging.info(f"Parsing '{raw_path}' ...")
    reader.import_raw(raw_path)
    reader.spectrum_df["scan"] = reader.spectrum_df.spec_idx.values+1
    reader.spectrum_df["activation_type"] = (
        reader.spectrum_df.scan_event_string.apply(
            get_activation_from_scan_event
        )
    )
    reader.spectrum_df.drop(columns="scan_event_string", inplace=True)
    reader.save_hdf(raw_path+".hdf5")
    with open(raw_path+".redo","w") as f:
        f.write("redo")
    return reader