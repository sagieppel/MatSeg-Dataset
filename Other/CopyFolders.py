import os
import shutil
indr="/mnt/306deddd-38b0-4adc-b1ea-dcd5efc989f3/MaterialsDataset/Multiphase_SmoothTransition_MultiObjects_Take2/"
outdr="/mnt/306deddd-38b0-4adc-b1ea-dcd5efc989f3/MaterialsDataset/MatSegDataset_Final/"
if not os.path.exists(outdr): os.mkdir(outdr)
xx=0
for ff, dr in enumerate(os.listdir(indr)):
    while (os.path.exists(outdr+"/"+str(xx))): xx+=1
    if os.path.exists(indr+"/"+dr+"/Finished.txt"):
        shutil.move(indr+"/"+dr,outdr+"/"+str(xx))
        print("moved:",indr+"/"+dr,outdr+"/"+str(xx))