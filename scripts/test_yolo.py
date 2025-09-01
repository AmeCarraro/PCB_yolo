import os
from ultralytics import YOLO

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"
SAVE_DIR = "C:\\Users\\carra\\Prova PCB\\runs"
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    # carica modello allenato
    model = YOLO("C:\\Users\\carra\\Prova PCB\\runs\\train\\PCB_defects\\weights\\best.pt")

    # predizione su tutto il test set
    results = model.predict(
        source=os.path.join(DST_ROOT, "test"),
        imgsz=640,
        save=True,
        project=SAVE_DIR,
        name="test_results",
        exist_ok=True  
    )
    print("✅ Predizioni salvate in:", results[0].save_dir)
