import numpy as np
import pandas as pd

activation_dict = {
    ord('h'): "ETHCD",
    ord('c'): "ETCID",
    ord('H'): "HCD",
    ord('E'): "ETD",
    ord('C'): "CID",
}

def get_activation_from_scan_event(scan_event_string:str):
    act_sub = scan_event_string[scan_event_string.find("@"):].upper()
    if "@HCD" in act_sub and "@ETD" in act_sub: return ord('h')
    elif "@CID" in act_sub and "@ETD" in act_sub: return ord('c')
    elif "@HCD" in act_sub: return ord('H')
    elif "@ETD" in act_sub: return ord('E')
    elif "@CID" in act_sub: return ord('C')
    else: return 0