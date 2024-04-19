import os

from alphabase.yaml_utils import load_yaml

CONST_FOLDER = os.path.dirname(__file__)

global_cfg = load_yaml(
    os.path.join(CONST_FOLDER, "default_cfg.yaml")
)

gwb_glyco_map = load_yaml(
    os.path.join(CONST_FOLDER, "glycoworkbench.yaml")
)