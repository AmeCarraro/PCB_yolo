# ===============================
# 5) Yolo testing
# ===============================

# YOLO tested on images without labels.
# The script loads the trained model and runs predictions on the entire test set,
# saving the results in the specified folder.

# YOLO testato su immagini senza label.
# Lo script carica il modello addestrato ed esegue predizioni sull'intero set di test,
# salvando i risultati nella cartella specificata.

import os
from ultralytics import YOLO

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"
SAVE_DIR = "C:\\Users\\carra\\Prova PCB\\runs"
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    # Load trained model
    model = YOLO("C:\\Users\\carra\\Prova PCB\\runs\\train\\PCB_defects\\weights\\best.pt")

    # Prediction on the entire test set
    results = model.predict(
        source=os.path.join(DST_ROOT, "test"),
        imgsz=640,
        save=True,
        project=SAVE_DIR,
        name="test_results",
        exist_ok=True  
    )
    print("Predictions saved in:", results[0].save_dir)
