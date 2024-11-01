# Photorealistic-3D-Reconstruction-with-Multi-view-Stereo
MVS with Broad Adaptive Checkerboard Sampling and Dynamic Multi-Hypothesis Joint View Selection, improvements based on ACMM

## Dependencies
The code has been tested on Ubuntu 14.04 with GTX Titan X.  
* [Cuda](https://developer.nvidia.com/zh-cn/cuda-downloads) >= 6.0
* [OpenCV](https://opencv.org/) >= 2.4
* [cmake](https://cmake.org/)
## Usage
* Compile ACMM
```  
cmake .  
make
```
* Test 
``` 
Use script colmap2mvsnet_acm.py to convert COLMAP SfM result to ACMM input   
Run ./ACMM $data_folder to get reconstruction results
