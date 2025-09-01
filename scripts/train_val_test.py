# ===============================
# 2) Train_Val_Test
# ===============================


# This script splits the PCB dataset images into train, validation, and test sets.
# Labels are copied for train and validation images, while test images are left without labels.
#
# Questo script divide le immagini del dataset PCB in set di train, validation e test.
# Le label vengono copiate per le immagini di train e validation, mentre le immagini di test rimangono senza label.


import os
import shutil
import random
import sys
from glob import glob

if __name__ == "__main__":
    
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Paths
    SRC_IMG = os.path.join(PROJECT_ROOT, "PCBDatasplit", "images")  # Path to the folder containing all images
    SRC_LAB = os.path.join(PROJECT_ROOT, "PCBDatasplit", "labels")  # Path to the folder containing all label files
    SPLIT_ROOT = os.path.join(PROJECT_ROOT, "PCBDatasplit", "split")  # Folder where the split datasets will be saved
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
            # Copy image
            shutil.copy(img, os.path.join(split_dir, base + ".jpg"))
            # Copy label
            if with_labels:
                lab = os.path.join(SRC_LAB, base.replace("_test","") + ".txt")
                if os.path.isfile(lab):
                    shutil.copy(lab, os.path.join(split_dir, base + ".txt"))

    copy_split(train_imgs, "train", True)
    copy_split(val_imgs, "val", True)
    copy_split(test_imgs, "test", False)

    print(f" Split completed in '{SPLIT_ROOT}': {n_train} train, {n_val} val, {len(test_imgs)} test")
