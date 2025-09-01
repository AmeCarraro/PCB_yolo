# ===============================
# 4) Yolo training
# ===============================


# Trains YOLOv8 on the PCB defect dataset, logs output to console and file,
# and runs validation at the end.

# Allena YOLOv8 sul dataset di difetti PCB, registra l'output su console e file,
# ed esegue la validazione al termine.


import os
from ultralytics import YOLO
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
DST_ROOT = os.path.join(PROJECT_ROOT, "PCBDatasplit", "split")
LOG_FILE = os.path.join(DST_ROOT, "training_log.txt")

# Class to write to both terminal and file simultaneously
class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for f in self.files:
            f.write(data)

    def flush(self):
        for f in self.files:
            f.flush()

if __name__ == "__main__":
    os.makedirs(DST_ROOT, exist_ok=True)
    log_file = open(LOG_FILE, "w", encoding="utf-8")
    sys.stdout = Tee(sys.stdout, log_file)
    sys.stderr = Tee(sys.stderr, log_file)

    # YOLO Training
    model = YOLO("yolov8n.pt")  # base model
    model.train(
        data=os.path.join(DST_ROOT, "data.yaml"),
        imgsz=640,
        epochs=100,
        batch=4,
        device=0,
        workers=0,
        verbose=True,
        project="runs/train",
        name="PCB_defects",
        exist_ok=True
    )

    # Validation at the end of training
    metrics = model.val(data=os.path.join(DST_ROOT, "data.yaml"))
    print("Validation metrics:", metrics)

    log_file.close()
