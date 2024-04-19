import copy

def get_glyco_compositions(canon):
    items = [item.strip(")") for item in canon.split("(")]
    comp_dict = {}
    for item in items:
        if item in comp_dict: comp_dict[item] += 1
        else: comp_dict[item] = 1
    return comp_dict

def composition_dict_to_str(comp_dict):
    return "".join(f"{g}({n})" for g,n in comp_dict.items())

def get_glyco_units(canon):
    return set([item.strip(")") for item in canon.split("(")])

def generate_subtrees_by_canons(canons):
    canon_set = set()
    for canon in canons:
        canon_set.update(generate_subtrees_by_canon(canon))
    return canon_set

def generate_subtrees_by_canon(canon):
    items = []
    start = 0
    for i in range(len(canon)):
        if canon[i] == "(" or canon[i] == ")":
            if start < i: items.append(canon[start:i])
            items.append(canon[i])
            start = i+1
    return canon_items_to_subtree_canons(items)
    
def canon_items_to_subtree_canons(items):
    root = items[1]
    branches = []
    left_count = 0
    start = 2
    for i in range(2, len(items)-1):
        if items[i] == "(":
            left_count += 1
        elif items[i] == ")":
            left_count -= 1
            if left_count == 0:
                branches.append(items[start:i+1])
                start = i+1
    
    branch_canons = set([""])
    for branch in branches:
        branch_codes = canon_items_to_subtree_canons(branch)
        tmp_set = copy.deepcopy(branch_canons)
        for subcode in branch_codes:
            for merge_canon in tmp_set:
                if (len(merge_canon), merge_canon) < (len(subcode), subcode): 
                    branch_canons.add(merge_canon + subcode)
                else: branch_canons.add(subcode + merge_canon)
    rooted_subcanons = set()
    for _code in branch_canons: 
        rooted_subcanons.add("(" + root + _code + ")")
    rooted_subcanons.add("")
    return rooted_subcanons