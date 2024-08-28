# MatSeg Dataset for Zero-Shot Class Agnostic Material Segmentation
The dataset and benchmark can be downloaded from :[1](https://zenodo.org/records/11331618), [2](https://e.pcloud.link/publink/show?code=kZHCcnZOfzqInb3anSl7xzFBoqCDmkr2JKV),[3](https://icedrive.net/s/SBb3g9WzQ5wZuxX9892Z3R4bW8jw).

Sample of the dataset available at  the [sample dir](https://github.com/sagieppel/MatSeg-Dataset/tree/main/sample).

See the paper [Learning Zero-Shot Material States Segmentation, by Implanting Natural Image Patterns in Synthetic Data](https://arxiv.org/pdf/2403.03309.pdf) for more details. 

# Description
MatSeg Dataset for Zero-Shot Material States Segmentation: The dataset contains large-scale synthetic images for training data and highly diverse real-world image benchmarks for testing. Focusing on zero-shot class-agnostic segmentation of materials and their states. This means finding the region of materials states without pre-training on the specific material classes or states. The benchmark contains a wide range of real-world materials and states. For example: wet regions of the surface, scattered dust, minerals of rocks, the sediment of soils, rotten parts of fruits, degraded and corrosive surface regions, food and liquid states, and many others. The focus is on scattered and fragmented materials, as well as soft boundaries partial transition, and partial similarity between regions. It contains both hard segmentation maps and soft and partial similarity annotations for similar but not identical materials


## Reader for the dataset
Reader for the dataset: [ReadAndDisplay.py](https://github.com/sagieppel/MatSeg-Dataset/blob/main/ReadAndDisplay.py).
Evaluation script for benchmark: [https://zenodo.org/records/13402003](https://zenodo.org/records/13402003) 


## Synthethic Training Dataset Structure
Each folder contains one image and its segmentation map.
RGB__RGB.jpg: The image rgb
Mask**.png: where ** a number of the mask of a given material, note materials can overlap and values can be between 0-255 (soft).

ObjectMaskOcluded.png: Basically the ROI mask means the region that is annotated, anything not marked in this mask is background and is not annotated.
![Figure 1](/Figure3.jpg)

## Real-world image Benchmark
 
A benchmark for zero-shot material state segmentation. The benchmark contains 820 real-world images with a wide range of material states and settings. For example: food states (cooked/burned..), plants (infected/dry.) to rocks/soil (minerals/sediment),  construction/metals (rusted, worn),  liquids  (foam/sediment), and many other states in a class-agnostic manner.  The goal is to evaluate the segmentation of material materials without knowledge or pretraining on the material or setting. The focus is on materials with complex scattered boundaries, and gradual transition  (like the level of wetness of the surface). The annotation of the benchmark is point-based and similarity-based. Hence, for each image, we select several points and regions (Figure 2). We group the points of the same materials into the same label, we also define a group of points that have partial similarity. For example points in group A are more similar to points in group B than to points in group C (In case materials A and B are similar to each other but not identical). This approach allows us to capture the complexity of gradual transition and partial similarities in the world. While also enabling dealing with complex scattered and blurry shapes without needing to annotate the full shape which in many cases is unclear or very hard
Evaluation scripts 

![Figure 1](/Figure4.jpg)
## Additional Data

See the paper: [Learning Zero-Shot Material States Segmentation, by Implanting Natural Image Patterns in Synthetic Data](https://arxiv.org/ftp/arxiv/papers/2403/2403.03309.pdf), for more details.

See the dataset generation script used to generate this data available at:
[https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script](https://github.com/sagieppel/MatSeg-Synthethic-Dataset-Generation-Script) 

