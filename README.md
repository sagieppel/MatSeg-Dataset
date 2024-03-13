# MatSeg Dataset for Zero-Shot Class Agnostic Material Segmentation
The dataset can be downloaded from : [1](https://e.pcloud.link/publink/show?code=kZHCcnZOfzqInb3anSl7xzFBoqCDmkr2JKV),[2](https://icedrive.net/s/SBb3g9WzQ5wZuxX9892Z3R4bW8jw)

## Reader for the dataset
Reader for the dataset: [ReadAndDisplay.py](https://github.com/sagieppel/MatSeg-Dataset/blob/main/ReadAndDisplay.py)
Sample of the dataset available at [/sample](https://github.com/sagieppel/MatSeg-Dataset/sample/)

## Dataset Structure
Each folder contains one image and its segmentation map.
RGB__RGB.jpg: The image rgb
Mask**.png: where ** a number of the mask of a given material, note materials can overlap and values can be between 0-255 (soft).

ObjectMaskOcluded.png: Basically the ROI mask means the region that is annotated, anything not marked in this mask is background and is not annotated.
![Figure 2](/Figure3.jpg)
## Additional Data

See paper: [Learning Zero-Shot Material States Segmentation, by Implanting Natural Image Patterns in Synthetic Data](https://arxiv.org/ftp/arxiv/papers/2403/2403.03309.pdf), for more details.

See dataset generation script used to generate this data available at:
[https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script](https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script) 

