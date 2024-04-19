import numba
import numpy as np
import pandas as pd
import tqdm
import typing

def merge_sister_ms2(
    spectrum_df:pd.DataFrame, 
    peak_df:pd.DataFrame,
    ppm_tol = 20.0,
    sister_scan_window = 10,
    keep_if_no_sisters = True,
)->typing.Tuple[pd.DataFrame,pd.DataFrame]:
    """
    Merge sister MS2 spectra which are triggered by the same MS1 precursor 
    into one merged spectrum for HCD-pd-XXD or other twin fragmentation methods.

    Args:
        spectrum_df (pd.DataFrame): The spectrum dataframe of a raw file
        peak_df (pd.DataFrame): the peak dataframe of a raw file
        ppm_tol (float, optional): PPM tolerance to merge peaks. Defaults to 20.0.
        sister_scan_window (int, optional): Scan window to find sister scans. Defaults to 10.
        keep_if_no_sisters (bool, optional): Keep the spectrum if no sisters are found. Defaults to True.

    Returns:
        pd.DataFrame: The merged spectrum dataframe
        pd.DataFrame: The merged peak dataframe
    """
    has_merged_spec_idxes = np.zeros(len(spectrum_df), dtype=np.uint8)
    new_spec_idxes = []
    new_mzs_list = []
    new_intens_list = []
    activation_list = []
    sisters_list = []
    for spec_idx in tqdm.tqdm(range(len(spectrum_df))):
        if has_merged_spec_idxes[spec_idx]: continue
        if spectrum_df.ms_level.values[spec_idx] == 1:
            new_spec_idxes.append(spec_idx)
            new_mzs_list.append(
                peak_df.mz.values[
                    spectrum_df.peak_start_idx.values[spec_idx]
                    :spectrum_df.peak_stop_idx.values[spec_idx]
                ]
            )
            new_intens_list.append(
                peak_df.intensity.values[
                    spectrum_df.peak_start_idx.values[spec_idx]
                    :spectrum_df.peak_stop_idx.values[spec_idx]
                ]
            )
            activation_list.append(0)
            sisters_list.append([spec_idx])
            continue
        sister_idxes = find_sister_idxes(spec_idx,
            spectrum_df.precursor_mz.values,
            spectrum_df.precursor_charge.values,
            spectrum_df.ms_level.values,
            spectrum_df.activation_id.values,
            sister_scan_window, 
            ignore_activation=0,
        )
        if len(sister_idxes) > 1:
            new_spec_idxes.append(spec_idx)
            new_mzs, new_intens = merge_sisters(
                peak_df.mz.values,
                peak_df.intensity.values,
                spectrum_df.peak_start_idx.values[sister_idxes],
                spectrum_df.peak_stop_idx.values[sister_idxes],
                ppm_tol,
            )
            new_mzs_list.append(new_mzs)
            new_intens_list.append(new_intens)
            has_merged_spec_idxes[sister_idxes] = 1
            activation_list.append(
                get_merged_activation(
                    np.unique(spectrum_df.activation_id.values[sister_idxes])
                )
            )
            sisters_list.append(sister_idxes)
        elif keep_if_no_sisters:
            new_spec_idxes.append(spec_idx)
            new_mzs_list.append(new_mzs)
            new_intens_list.append(new_intens)
            activation_list.append(spectrum_df.activation_id.values[spec_idx])
            sisters_list.append([spec_idx])

    new_spec_df, new_peak_df = create_new_spec_peak_df(
        spectrum_df, new_spec_idxes,
        new_mzs_list, new_intens_list,
        activation_list
    )
    sister_map_df = pd.DataFrame(dict(
        spec_idx = [x[0] for x in sisters_list],
        sister_idx = [x[1:] for x in sisters_list],
    ))
    sister_map_df = sister_map_df.explode(
        "sister_idx"
    ).dropna().reset_index(drop=True)
    sister_map_df = sister_map_df.astype(np.int64)
    return new_spec_df, new_peak_df, sister_map_df

def create_new_spec_peak_df(
    spectrum_df:pd.DataFrame, 
    new_spec_idxes,
    mzs_list, intens_list, 
    activation_list
)->typing.Tuple[pd.DataFrame,pd.DataFrame]:
    peak_indices = np.empty(len(mzs_list)+1,dtype=np.int64)
    peak_indices[0] = 0
    peak_indices[1:] = np.cumsum([len(x) for x in mzs_list])
    peak_df = pd.DataFrame(dict(
        mz = np.concatenate(mzs_list),
        intensity = np.concatenate(intens_list)
    ))
    new_spec_df = spectrum_df.iloc[new_spec_idxes,:].copy()
    new_spec_df["old_spec_idx"] = new_spec_idxes
    new_spec_df = new_spec_df.reset_index(drop=True)
    new_spec_df["peak_start_idx"] = peak_indices[:-1]
    new_spec_df["peak_stop_idx"] = peak_indices[1:]
    new_spec_df["spec_idx"] = new_spec_df.index.values
    new_spec_df["activation_id"] = activation_list
    return new_spec_df, peak_df

@numba.njit
def find_sister_idxes(cur_idx, 
    precursor_mzs, charges, 
    ms_levels, activation_ids, 
    search_scan_window,
    ignore_activation=ord('H'),
):
    activation_found = np.zeros(128, dtype=np.uint8)
    activation_found[ignore_activation] = 1
    cur_mz = precursor_mzs[cur_idx]
    cur_ch = charges[cur_idx]
    sister_idxes = [cur_idx]
    if cur_mz < 1 or cur_ch == 0: return sister_idxes
    # find forward
    for i in range(cur_idx+1, cur_idx+search_scan_window):
        if i >= len(charges): break
        if (
            activation_found[activation_ids[i]] == 1
            or ms_levels[i] == 1
        ): continue
        if abs(precursor_mzs[i]-cur_mz)<=1e-5 and charges[i]==cur_ch:
            sister_idxes.append(i)
            activation_found[activation_ids[i]] = 1
    ## find backward (not necessary)
    # for i in range(cur_idx-1, cur_idx-search_scan_window, -1):
    #     if i < 0: break
    #     if (
    #         ms_levels[i] == 1 or 
    #         activation_found[activation_ids[i]] == 1
    #     ): continue
    #     if abs(precursor_mzs[i]-cur_mz)<=1e-5 and charges[i]==cur_ch:
    #         sister_idxes.append(i)
    #         activation_found[activation_ids[i]] = 1
    return sister_idxes

@numba.njit
def merge_sisters(
    peak_mzs, peak_intens,
    peak_start_idxes, peak_stop_idxes,
    ppm_tol,
):
    ret_mzs = peak_mzs[peak_start_idxes[0]:peak_stop_idxes[0]]
    ret_intens = peak_intens[peak_start_idxes[0]:peak_stop_idxes[0]]
    for i in range(1, len(peak_start_idxes)):
        ret_mzs, ret_intens = merge_one_sister(
            ret_mzs, ret_intens, 
            peak_mzs[peak_start_idxes[i]:peak_stop_idxes[i]],
            peak_intens[peak_start_idxes[i]:peak_stop_idxes[i]],
            ppm_tol=ppm_tol
        )
    return ret_mzs, ret_intens

def get_merged_activation(unique_act_ids:np.ndarray):
    if len(unique_act_ids) == 1: return unique_act_ids[0]
    max_id = unique_act_ids.max()
    if max_id == ord('h') or max_id == ord('c'): return ord('h')
    if ord('H') in unique_act_ids and ord('E') in unique_act_ids: 
        return ord('h')
    return ord('H')

@numba.njit
def merge_one_sister(
    peak_mzs1, peak_intens1,
    peak_mzs2, peak_intens2,
    ppm_tol,
):
    ret_mzs = []
    ret_intens = []
    mz_tols = peak_mzs1*ppm_tol*1e-6
    i,j = 0,0
    while i < len(peak_mzs1) and j < len(peak_mzs2):
        if abs(peak_mzs1[i]-peak_mzs2[j]) <= mz_tols[i]:
            ret_intens.append(peak_intens1[i]+peak_intens2[j])
            ret_mzs.append(
                (peak_intens1[i]*peak_mzs1[i]+peak_intens2[j]*peak_mzs2[j])
                / (ret_intens[-1])
            )
            i += 1
            j += 1
        elif peak_mzs1[i] > peak_mzs2[j]: 
            ret_intens.append(peak_intens2[j])
            ret_mzs.append(peak_mzs2[j])
            j += 1
        else: 
            ret_intens.append(peak_intens1[i])
            ret_mzs.append(peak_mzs1[i])
            i += 1
    if i < len(peak_mzs1):
        ret_mzs.extend(peak_mzs1[i:])
        ret_intens.extend(peak_intens1[i:])
    elif j < len(peak_mzs2):
        ret_mzs.extend(peak_mzs2[j:])
        ret_intens.extend(peak_intens2[j:])
    ret_mzs = np.array(ret_mzs, dtype=peak_mzs1.dtype)
    sorted_idxes = np.argsort(ret_mzs)
    return (
        ret_mzs[sorted_idxes], 
        np.array(ret_intens, dtype=peak_intens1.dtype)[sorted_idxes]
    )

