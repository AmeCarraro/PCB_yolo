import os
from ultralytics import YOLO
import sys

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"
LOG_FILE = os.path.join(DST_ROOT, "training_log.txt")

# ===============================
# Classe per scrivere su terminale e file contemporaneamente
# ===============================
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

    # apertura log file
    log_file = open(LOG_FILE, "w", encoding="utf-8")

    # sys.stdout e sys.stderr vanno sia a terminale che a file
    sys.stdout = Tee(sys.stdout, log_file)
    sys.stderr = Tee(sys.stderr, log_file)

    # ===============================
    # Addestramento YOLO
    # ===============================
    model = YOLO("yolov8n.pt")  # modello base
    model.train(
        data=os.path.join(DST_ROOT, "data.yaml"),
        imgsz=640,
        epochs=100,
        batch=4,
        device=0,
        workers=0,
        verbose=True,  # serve a mostrare output dettagliato
        project="runs/train",
        name="PCB_defects",
        exist_ok=True
    )

    # ===============================
    # Validazione al termine del training
    # ===============================
    metrics = model.val(data=os.path.join(DST_ROOT, "data.yaml"))
    print("📊 Metriche validation:", metrics)

    # chiusura log
    log_file.close()
