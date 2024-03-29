# Reduce value below 15 to zero in all masks (assume this values are close to zero and noise) also this dramatically reduce file sizes.
# For some reason the masks generated by Blender have white noise of values 0-10 that doesnt really shown, or do anything but add massively to the file size
# This script read al the masks in the data and replace values below 15 to zero, hence reduce the dataset size by factor of 5.
import os
import cv2
# path to dataset main dir
MatSegDir = "out_generated_data/"
for dr in os.listdir(MatSegDir):
    path = MatSegDir+"/"+dr
    if os.path.isdir(path):
        for fl in os.listdir(path):
            if "mask" in fl or "Mask" in fl:
                im=cv2.imread(path+"/"+fl,0)
                im[im<15]=0
                cv2.imwrite(path+"/"+fl,im)
                print(path+"/"+fl)


