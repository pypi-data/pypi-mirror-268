import os
import pandas as pd

from pglyco.utils.logger import logging
from pglyco.const import gwb_glyco_map
from pglyco.utils.canon import (
    generate_subtrees_by_canons, 
    get_glyco_compositions,
    composition_dict_to_str
)

def parse_gwp(
    input_gwp_file,
    output_gdb_file,
    max_len = 100,
):
    logging.info(f"Parsing {input_gwp_file} ...")
    gwb_struct_list = load_gwp(input_gwp_file)
    logging.info(f"Loaded {len(gwb_struct_list)} gwb structures ...")
    canons = gwb_structs_to_canons(gwb_struct_list)

    canons = list(generate_subtrees_by_canons(canons))
    logging.info(f"Generated {len(canons)} pGlyco sub-structures ...")
    canons.sort(key = lambda x: (len(x), x))

    logging.info(f"Save as {os.path.abspath(output_gdb_file)}")
    df = pd.DataFrame(dict(
        structure_code = canons
    ))
    df["composition"] = df.structure_code.apply(lambda x:
        composition_dict_to_str(get_glyco_compositions(x))
    )
    df["n_glyco"] = df.structure_code.str.count("(")
    df = df.query(f"n_glyco <= {max_len} and n_glyco > 0")
    df.to_csv(output_gdb_file, index=False, sep='\t')

def load_gwp(gwp):
    gwb_struct_list = []
    with open(gwp) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("<Glycan structure="):
                glystruct = line[line.find('"')+1:line.rfind('"')]
                gwb_struct_list.append(glystruct)
    return gwb_struct_list

def gwb_structs_to_canons(gwb_struct_list):
    canons = set()
    for gwb_struct in gwb_struct_list:
        canons.update(gwb_struct_to_canon(gwb_struct))
    return canons

def gwb_struct_to_canon(gwb_struct):
    find_dict = {}
    for key in gwb_glyco_map.keys():
        find_dict[key] = str_find_all_substr(
            gwb_struct, key+",p"
        )
    left_ = str_find_all_substr(gwb_struct, '(')
    right_ = str_find_all_substr(gwb_struct, ')')
    items = []
    for key, vals in find_dict.items():
        for val in vals:
            items.append((val, gwb_glyco_map[key]))
    for val in left_:
        items.append((val, '('))
    for val in right_:
        items.append((val, ')'))
    items.sort()
    items = [item[1] for item in items]
    return _gwb_items_to_canon(items)
    
def _gwb_items_to_canon(items):
    root_items = []
    i = 0
    while i < len(items):
        if items[i]  == "(": break
        root_items.append(items[i])
        i += 1
    return "("+"(".join(root_items)+"".join(items[i:]+")"*len(root_items))

def str_find_all_substr(s, sub):
    ret = []
    idx = s.find(sub)
    while idx != -1:
        ret.append(idx)
        idx = s.find(sub, idx+1)
    return ret

# print(generate_subtree_by_canon("(N(H(A))(H(A)))"))

                