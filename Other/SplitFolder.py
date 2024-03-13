import os
import shutil
import numpy as np
indr="/mnt/306deddd-38b0-4adc-b1ea-dcd5efc989f3/MaterialsDataset/Merged//"
outdr="/mnt/306deddd-38b0-4adc-b1ea-dcd5efc989f3/MaterialsDataset/MatSegDataset_Split/"
if not os.path.exists(outdr): os.mkdir(outdr)
split=2000
for i in range(100000):
    outsub = outdr+"/"+str(int(np.floor(i/split)))
    if not os.path.exists(outsub): os.mkdir(outsub)
    if os.path.exists(indr+"/"+str(i)+"/Finished.txt"):
        shutil.move(indr+"/"+str(i),outsub+"/"+str(i))