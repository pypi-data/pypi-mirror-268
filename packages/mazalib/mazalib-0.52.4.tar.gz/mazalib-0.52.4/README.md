# MAZAlib

Cross-platform 2d/3d image segmentation C++ library

Authors: Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina, Andrey A. Ananev
Moscow, 2017-2024

## Prerequisites

### Install a modern C++ compiler.
Mac OS: 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && xcode-select --install
```
Linux (Ubuntu): 
```
sudo apt-get install g++
```

Windows: Visual Studio 2015 or later with C++ tools installed

### Install MazaLib

The easiest way to install and run **MAZAlib** is to utilize Python virtual environments (below are the commands to setup **MAZAlib** in Unix-based operation system, similar approach can be applied under Windows):

1. Here env_name is any environment name that will used to run **MAZAlib**. path_to_env - path to the environment where it will be created (Use '.') if it's current folder.
```
python -m venv path_to_env/env_name
source path_to_env/env_name/bin/activate
```
2. Note that under Unix-based systems you might need to install gtk library `pip install numpy mazalib`. Next, invoke following python code to activate GUI: (example run unsharp filter)
```
import numpy as np
import mazalib

im = np.fromfile('path/to/image.raw', dtype='uint8')
side_size = int(round(im.size**(1/3)))
im = np.reshape(im, (side_size,side_size,side_size))
result = mazalib.unsharp(im, [3.0])
```

# Implemented approaches

Binarization (segmentation into two phases):

1. Indicator kriging (Oh, W., & Lindquist, B. (1999). Image thresholding by indicator kriging. IEEE Transactions on Pattern Analysis and Machine Intelligence, 21(7), 590–602) [link](https://ieeexplore.ieee.org/abstract/document/777370)

2. Markov random field aka MRF (Kulkarni, R., Tuller, M., Fink, W., & Wildenschild, D. (2012). Three-dimensional multiphase segmentation of X-ray CT data of 
porous materials using a Bayesian Markov random field framework. Vadose Zone Journal, 11(1)) [link](https://acsess.onlinelibrary.wiley.com/doi/epdf/10.2136/vzj2011.0082)

3. Region growth aka RG (Hashemi, M. A., Khaddour, G., François, B., Massart, T. J., & Salager, S. (2014). A tomographic imagery segmentation methodology for three-phase geomaterials based on simultaneous region growing. Acta Geotechnica, 9, 831-846) [link](https://link.springer.com/article/10.1007/s11440-013-0289-5)
4. Converging active contours aka CAC (Sheppard, A. P., Sok, R. M., & Averdunk, H. (2004). Techniques for image enhancement and segmentation of tomographic images of porous materials. Physica A: Statistical mechanics and its applications, 339(1-2), 145-151) [link](https://www.sciencedirect.com/science/article/abs/pii/S037843710400370X)

Filters:
1. Unsharp mask
2. Non-local means (we added NLM implementation by Bruns, S., Stipp, S. L. S., & Sørensen, H. O. (2017). Looking for the signal: A guide to iterative noise and artefact removal in X-ray tomographic reconstructions of porous geomaterials. Advances in Water Resources, 105, 96-107) [link](https://www.sciencedirect.com/science/article/abs/pii/S030917081630598X)


# Publications

The paper describing this library is currently submitted to Computers & Geosciences Journal.

# Useful cross-references
1. MAZAgui -  to utilize graphical user interface for [MAZAlib](https://pypi.org/project/mazagui/)
2. PyFDMSS - a library to simulate single-phase flow on binary 3D pore geometries (Gerke, K. M., Vasilyev, R. V., Khirevich, S., Collins, D., Karsanina, M. V., Sizonenko, T. O., Korost, D.V., Lamontagne, S. & Mallants, D. (2018). Finite-difference method Stokes solver (FDMSS) for 3D pore geometries: Software development, validation and case studies. Computers & geosciences, 114, 41-58) [link](https://www.sciencedirect.com/science/article/abs/pii/S0098300417306234) : [pyfdmss](https://pypi.org/project/pyfdmss/)