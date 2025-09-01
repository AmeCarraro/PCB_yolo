# ===============================
# 1) Data Handler
# ===============================

# This script scans all subfolders in the PCB dataset, copies `_test` images to a destination folder,
# and converts the corresponding `.txt` annotations to YOLO format, ignoring background labels.
# 
# Questo script esplora tutte le sottocartelle del dataset PCB, copia le immagini `_test` in una cartella
# di destinazione e converte le annotazioni `.txt` corrispondenti nel formato YOLO, ignorando le etichette di background.


import os
import shutil
from glob import glob
from PIL import Image

# Source and destination folders
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_ROOT = os.path.join(PROJECT_ROOT, "PCBData")
DST_ROOT = os.path.join(PROJECT_ROOT, "PCBDatasplit")

DST_IMG = os.path.join(DST_ROOT, "images")
DST_LAB = os.path.join(DST_ROOT, "labels")

# Create output folders if they do not exist
os.makedirs(DST_IMG, exist_ok=True)
os.makedirs(DST_LAB, exist_ok=True)

# Scan all subfolders in PCBData
for subdir in os.listdir(SRC_ROOT):
    full_path = os.path.join(SRC_ROOT, subdir)
    if not os.path.isdir(full_path):
        continue

    # Locate the "_not" folder and the regular folder
    subfolders = [os.path.join(full_path, d) for d in os.listdir(full_path) if os.path.isdir(os.path.join(full_path, d))]
    for sf in subfolders:
        if "_not" in os.path.basename(sf).lower():
            # Copy and format ALL txt files
            for txt_file in glob(os.path.join(sf, "*.txt")):
                base = os.path.splitext(os.path.basename(txt_file))[0]
                dst_txt_path = os.path.join(DST_LAB, os.path.basename(txt_file))

                # Attempt to find the corresponding _test image
                img_path = None
                for ext in [".jpg", ".png", ".jpeg"]:
                    candidate = os.path.join(DST_IMG, base + "_test" + ext)
                    if os.path.isfile(candidate):
                        img_path = candidate
                        break

                # If the image is not found, copy the txt file as is
                if img_path is None:
                    shutil.copy(txt_file, dst_txt_path)
                    continue

                with Image.open(img_path) as im:
                    W, H = im.size

                lines_out = []
                with open(txt_file, "r") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        # Separator can be a space or a comma
                        parts = line.replace(",", " ").split()
                        if len(parts) != 5:
                            continue
                        try:
                            x1, y1, x2, y2 = map(float, parts[:4])
                            typ = int(parts[4])
                        except:
                            continue

                        if typ == 0:  # background → ignore
                            continue
                        cls = typ - 1  # map 1..6 to 0..5

                        # clamp box
                        x1, x2 = max(0, x1), min(W, x2)
                        y1, y2 = max(0, y1), min(H, y2)
                        if x2 <= x1 or y2 <= y1:
                            continue

                        xc = ((x1 + x2)/2) / W
                        yc = ((y1 + y2)/2) / H
                        bw = (x2 - x1) / W
                        bh = (y2 - y1) / H

                        lines_out.append(f"{cls} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

                with open(dst_txt_path, "w") as f:
                    f.write("\n".join(lines_out))

        else:
            # Copy only _test images
            for img in glob(os.path.join(sf, "*_test.*")):
                shutil.copy(img, DST_IMG)

print("Copying and conversion completed!")
