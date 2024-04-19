import pandas as pd
import tqdm

from pglyco.raw_data.raw_utils import activation_dict

def df_to_ms1_ms2_for_pParse(
    raw_path:str,
    spectrum_df:pd.DataFrame, 
    peak_df:pd.DataFrame,
):
    with (
        open(raw_path[:-4]+".ms1", "w", 16*1024*1024) as ms1, 
        open(raw_path[:-4]+".ms2", "w", 16*1024*1024) as ms2,
    ):
        ms1.write("""H  CreationDate    Empty
H   Extractor   pGlyco3Raw
H   ExtractorVersion    1.0.0
H   Comments    For pGlyco Only
H   DataType    Centroid
H   Vendor  Thermo
H   Instrument  Orbitrap
H   Duration    0
H   DDA\n""")
        
        ms2.write("""H  CreationDate    Empty
H   Extractor   AlphaRaw
H   ExtractorVersion    1.0.0
H   Comments    For pGlyco Only
H   DataType    Centroid
H   Vendor  Thermo
H   Instrument  Orbitrap
H   Duration    0
H   DDA\n""")

    last_ms1_scan = 1
    for (
        scan, peak_start, peak_stop, 
        mz, charge, rt, ms_level,
        isolation_lower_mz, isolation_upper_mz,
        scan_event_string,
    ) in tqdm.tqdm(spectrum_df[[
        "scan","peak_start_idx","peak_stop_idx", 
        "precursor_mz", "precursor_charge", "rt", "ms_level",
        "isolation_lower_mz", "isolation_upper_mz",
        "scan_event_string",
    ]].values):
        scan = int(scan)
        peak_start = int(peak_start)
        peak_stop = int(peak_stop)
        mz = float(mz)
        charge = int(charge)
        rt_sec = float(rt)*60
        center = (float(isolation_lower_mz)+float(isolation_upper_mz))/2
        if ms_level == 1:
            last_ms1_scan = scan
            write_one_ms1(
                ms1, scan, rt_sec,
                peak_df.mz.values[peak_start:peak_stop],
                peak_df.intensity.values[peak_start:peak_stop],
            )
        else:
            write_one_ms2(
                ms2, scan, last_ms1_scan, rt_sec,
                mz, charge, center, scan_event_string,
                peak_df.mz.values[peak_start:peak_stop],
                peak_df.intensity.values[peak_start:peak_stop],
            )

def write_one_ms1(ms1, scan, rt_sec, peak_mzs, peak_intens):
    ms1.write(f"S\t{scan}\t{scan}\n")
    ms1.write(f"I\tNumberOfPeaks\t{len(peak_mzs)}\n")
    ms1.write(f"I\tRetTime\t{rt_sec:.6f}\n")
    ms1.write("I\tIonInjectionTime\t1\n")
    ms1.write("I\tInstrumentType\tFTMS\n")
    for mass, inten in zip(peak_mzs, peak_intens):
        ms1.write(f"{mass:.5f} {inten:.1f}\n")

def write_one_ms2(
    ms2, scan, last_ms1_scan, rt_sec, mz, charge, center,
    activation_id, peak_mzs, peak_intens
):
    if charge == 0: charge == 2
    if mz < 1: mz = center

    if not activation_type: return
    activation_type = activation_dict[activation_id]

    mono_mass = (mz-1.007276)*charge+1.007276
    ms2.write(f"S\t{scan}\t{scan}\t{mz:.6f}\n")
    ms2.write(f"I\tNumberOfPeaks\t{len(peak_mzs)}\n")
    ms2.write(f"I\tRetTime\t{rt_sec:.6f}\n")
    ms2.write("I\tIonInjectionTime\t1\n")
    ms2.write(f"I\tActivationType\t{activation_type}\n")
    ms2.write("I\tInstrumentType\tFTMS\n")
    ms2.write(f"I\tPrecursorScan\t{last_ms1_scan}\n")
    ms2.write(f"I\tActivationCenter\t{center:.6f}\n")
    ms2.write(f"I\tMonoiosotopicMz\t{mz}\n")
    ms2.write(f"Z\t{charge}\t{mono_mass:.6f}\n")
    for mass, inten in zip(peak_mzs, peak_intens):
        ms2.write(f"{mass:.5f} {inten:.1f}\n")