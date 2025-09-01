# ===============================
# 3) File data.yaml
# ===============================


# This script creates a `data.yaml` file for the YOLO training pipeline,
# specifying the dataset path, train/val/test folders, and the class names for PCB defects.
#
# Questo script crea un file `data.yaml` per la pipeline di training YOLO,
# specificando il percorso del dataset, le cartelle train/val/test e i nomi delle classi dei difetti PCB.


import yaml    
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST_ROOT = os.path.join(PROJECT_ROOT, "PCBDatasplit", "split")

data_yaml = {
    "path": DST_ROOT,
    "train": "train",
    "val": "val",
    "test": "test",
    "names": {
        0: "open", 1: "short", 2: "mousebite", 3: "spur", 4: "copper", 5: "pin-hole"
    }
}
os.makedirs(DST_ROOT, exist_ok=True)
with open(os.path.join(DST_ROOT, "data.yaml"), "w") as f:
    yaml.dump(data_yaml, f, default_flow_style=False)
print("data.yaml created")
