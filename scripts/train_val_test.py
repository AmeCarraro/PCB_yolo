#questo codice va a dividere le immaigni in una cartella split, dividendole in train validation e test
#nel caso di train e validation saranno ovviamente inserite anche le relative labels, mentre in test no

import os
import shutil
import random
import sys
from glob import glob

if __name__ == "__main__":
    # ===============================
    # 1) Split dataset
    # ===============================
    SRC_IMG = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\images"
    SRC_LAB = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\labels"
    SPLIT_ROOT = "C:\\Users\\carra\\Prova PCB\\PCBDatasplit\\split"  # cartella per i risultati
    os.makedirs(SPLIT_ROOT, exist_ok=True)

    for split in ["train", "val", "test"]:
        os.makedirs(os.path.join(SPLIT_ROOT, split), exist_ok=True)

    all_imgs = glob(os.path.join(SRC_IMG, "*_test.*"))
    random.shuffle(all_imgs)
    n = len(all_imgs)
    n_train, n_val = int(0.7 * n), int(0.2 * n)
    train_imgs = all_imgs[:n_train]
    val_imgs = all_imgs[n_train:n_train+n_val]
    test_imgs = all_imgs[n_train+n_val:]

    def copy_split(imgs, split, with_labels=True):
        split_dir = os.path.join(SPLIT_ROOT, split)
        for img in imgs:
            base = os.path.splitext(os.path.basename(img))[0]
            # copia immagine
            shutil.copy(img, os.path.join(split_dir, base + ".jpg"))
            # copia label
            if with_labels:
                lab = os.path.join(SRC_LAB, base.replace("_test","") + ".txt")
                if os.path.isfile(lab):
                    shutil.copy(lab, os.path.join(split_dir, base + ".txt"))

    copy_split(train_imgs, "train", True)
    copy_split(val_imgs, "val", True)
    copy_split(test_imgs, "test", False)

    print(f"✅ Split completato in '{SPLIT_ROOT}': {n_train} train, {n_val} val, {len(test_imgs)} test")
