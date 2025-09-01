import os
import random
from ultralytics import YOLO

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"
SAVE_DIR = "C:\\Users\\carra\\Prova PCB\\runs"
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    model = YOLO("C:\\Users\\carra\\Prova PCB\\runs\\train\\PCB_defects\\weights\\best.pt")

    # scegli immagine a caso dalla cartella test
    test_images = os.listdir(os.path.join(DST_ROOT, "test"))
    img_path = os.path.join(DST_ROOT, "test", random.choice(test_images))

    print(f"🔍 Predizione su: {img_path}")
    results = model.predict(
        source=img_path,
        imgsz=640,
        save=True,
        project=SAVE_DIR,     # cartella principale dove salvare
        name="single_try",    # sottocartella per questa predizione
        exist_ok=True         # sovrascrive se già esiste
    )
    print("✅ Predizione salvata in:", results[0].save_dir)
