import yaml    
import os
# ===============================
# 2) File data.yaml
# ===============================

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"

data_yaml = {
    "path": DST_ROOT,
    "train": "train",
    "val": "val",
    "test": "test",
    "names": {
        0: "open", 1: "short", 2: "mousebite", 3: "spur", 4: "copper", 5: "pin-hole"
    }
}
with open(os.path.join(DST_ROOT, "data.yaml"), "w") as f:
    yaml.dump(data_yaml, f, default_flow_style=False)
print("data.yaml creato")
