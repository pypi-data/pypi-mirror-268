import pandas as pd
import os
import logging

def df_to_mgf(
    raw_path:str,
    spectrum_df:pd.DataFrame,
    peak_df:pd.DataFrame
):
    dir_name, raw_name = os.path.split(raw_path)
    raw_name = os.path.splitext(raw_name)[0]
    with open(
        os.path.join(dir_name, "~"+raw_name+".mgf"), 
        "w", buffering=16*1024*1024
    ) as mgf:
        for (
            scan, peak_start, peak_stop, 
            mz, charge, rt, ms_level,
        ) in spectrum_df[[
            "scan", "peak_start_idx", "peak_stop_idx", 
            "precursor_mz", "precursor_charge", "rt", "ms_level",
        ]].values:
            if ms_level == 1: continue
            start = int(peak_start)
            stop = int(peak_stop)
            _write_one_mgf(mgf,
                raw_name, int(scan), mz, int(charge), rt*60,
                peak_mzs=peak_df.mz.values[start:stop],
                peak_intens=peak_df.intensity.values[start:stop],
            )
    os.rename(
        os.path.join(dir_name, "~"+raw_name+".mgf"),
        os.path.join(dir_name, raw_name+".mgf")
    )

def _write_one_mgf(f, 
    raw_name, scan, 
    mz, charge, rt_sec,
    peak_mzs, peak_intens,
):
    f.write("BEGIN IONS\n")
    f.write(f"TITLE={raw_name}.{scan}.{scan}.{charge}.0.dta\n")
    f.write(f"SCAN={scan}\n")
    f.write(f"RTINSECONDS={rt_sec:6f}\n")
    f.write(f"CHARGE={charge}+\n")
    f.write(f"PEPMASS={mz:8f}\n")
    for mass, inten in zip(peak_mzs, peak_intens):
        f.write(f"{mass:.5f} {inten:.1f}\n")
    f.write("END IONS\n")