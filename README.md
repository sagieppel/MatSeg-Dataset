# MatSeg Dataset for Zero-Shot Class Agnostic Material Segmentation
The dataset can be downloaded from : [1](https://e.pcloud.link/publink/show?code=kZHCcnZOfzqInb3anSl7xzFBoqCDmkr2JKV),[2](https://icedrive.net/s/SBb3g9WzQ5wZuxX9892Z3R4bW8jw)
# Dataset Structure
Each folder contains one image and its segmentation map.
RGB__RGB.jpg: The image rgb
Mask**.png: where ** a number of the mask of a given material, note materials can overlap and values can be between 0-255 (soft).

ObjectMaskOcluded.png: Basically the ROI mask means the region that is annotated, anything not marked in this mask is background and is not annotated.


See paper: [Learning Zero-Shot Material States Segmentation, by Implanting Natural Image Patterns in Synthetic Data](https://arxiv.org/ftp/arxiv/papers/2403/2403.03309.pdf), for more details.

See dataset generation script used to generate this data available at:
[https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script](https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script) 


1) The MatSeg Benchmark (real images) is Available at [1](https://icedrive.net/s/NtbARDSx6WtSN748Z7kix8ZXZtSu),[2](https://e.pcloud.link/publink/show?code=XZDsGnZ3ERMX76L5dYLzfnPTch8fYRtlRXV)
2) MatSeg Dataset Generation Script (blender/python): [https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script](https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script)
3) The Synthetic DataSet is available at:  [1](https://e.pcloud.link/publink/show?code=kZHCcnZOfzqInb3anSl7xzFBoqCDmkr2JKV),[2](https://icedrive.net/s/SBb3g9WzQ5wZuxX9892Z3R4bW8jw)
