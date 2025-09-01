import os
import shutil
from glob import glob
from PIL import Image

# cartelle di origine e destinazione
SRC_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBData"
DST_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit"

DST_IMG = os.path.join(DST_ROOT, "images")
DST_LAB = os.path.join(DST_ROOT, "labels")

# crea cartelle di output se non esistono
os.makedirs(DST_IMG, exist_ok=True)
os.makedirs(DST_LAB, exist_ok=True)

# scorri tutte le sottocartelle dentro PCBData
for subdir in os.listdir(SRC_ROOT):
    full_path = os.path.join(SRC_ROOT, subdir)
    if not os.path.isdir(full_path):
        continue

    # cerca la cartella con "_not" e quella senza
    subfolders = [os.path.join(full_path, d) for d in os.listdir(full_path) if os.path.isdir(os.path.join(full_path, d))]
    for sf in subfolders:
        if "_not" in os.path.basename(sf).lower():
            # copia e formatta TUTTI i txt
            for txt_file in glob(os.path.join(sf, "*.txt")):
                base = os.path.splitext(os.path.basename(txt_file))[0]
                dst_txt_path = os.path.join(DST_LAB, os.path.basename(txt_file))

                # tenta trovare immagine corrispondente _test
                img_path = None
                for ext in [".jpg", ".png", ".jpeg"]:
                    candidate = os.path.join(DST_IMG, base + "_test" + ext)
                    if os.path.isfile(candidate):
                        img_path = candidate
                        break

                # se immagine non trovata, copia txt così com’è
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
                        # separatore può essere spazio o virgola
                        parts = line.replace(",", " ").split()
                        if len(parts) != 5:
                            continue
                        try:
                            x1, y1, x2, y2 = map(float, parts[:4])
                            typ = int(parts[4])
                        except:
                            continue

                        if typ == 0:  # background → ignora
                            continue
                        cls = typ - 1  # mappa 1..6 → 0..5

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
            # copia solo immagini _test
            for img in glob(os.path.join(sf, "*_test.*")):
                shutil.copy(img, DST_IMG)

print("✅ Copiatura e conversione completate!")
