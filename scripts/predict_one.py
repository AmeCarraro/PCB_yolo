#Code to test on a single random image

import os
import random
from ultralytics import YOLO

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DST_ROOT = os.path.join(PROJECT_ROOT, "PCBDatasplit", "split")
SAVE_DIR = os.path.join(PROJECT_ROOT, "runs")
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    MODEL_PATH = os.path.join(PROJECT_ROOT, "runs", "train", "PCB_defects", "weights", "best.pt")
    model = YOLO(MODEL_PATH)

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
