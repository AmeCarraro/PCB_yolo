#Code to test on a single random image

import os
import random
from ultralytics import YOLO

DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"
SAVE_DIR = "C:\\Users\\carra\\Prova PCB\\runs"
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    model = YOLO("C:\\Users\\carra\\Prova PCB\\runs\\train\\PCB_defects\\weights\\best.pt")

    # Random image to test
    test_images = os.listdir(os.path.join(DST_ROOT, "test"))
    img_path = os.path.join(DST_ROOT, "test", random.choice(test_images))

    print(f"Prediction on: {img_path}")
    results = model.predict(
        source=img_path,
        imgsz=640,
        save=True,
        project=SAVE_DIR,
        name="single_try",
        exist_ok=True
    )
    print("Prediction saved in:", results[0].save_dir)
