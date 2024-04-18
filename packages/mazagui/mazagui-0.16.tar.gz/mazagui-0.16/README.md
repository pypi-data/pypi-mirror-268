# MAZAlib

GUI for MazaLib (cross-platform 2d/3d image segmentation C++ library)

Authors: Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina, Andrey A. Ananev
Moscow, 2017-2024

## Prerequisites (for MazaLib)

Install a modern C++ compiler.

Mac OS: 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && xcode-select --install
```
Linux (Ubuntu): 
```
sudo apt-get install g++
```

Windows: Visual Studio 2015 or later with C++ tools installed

# Usage

![GUI image](https://github.com/DreamerAA/mazagui/blob/main/MAZAgui.jpg?raw=True)

1. Load a binary file using context menu (1) File -> Load a file.
2. Choose preprocessing method using menu (2): Unsharp (Unsharp mask – Sobel filter), NLM (Non-Local Means filter), None. Note that after filtration step you need to push “<-“ button above in order to move the results to the left subwindow.
3. Choose segmentation method using menu (3): Indicator Kriging (IK), Converging Active Contours (CAC), Markov Random Fields (MRF), Region Growing Segmentation (RGS), None.
4. Edit default configuration parameters for different methods, if necessary, in menu (4).
5. Choose lower and upper thresholds in menu (5).
6. Launch segmentation using button “Run” (6).
7. Examine result slice by slice using slider (7).
8. Save result as a .raw file using context menu (8) File -> Save as a file.

# Useful cross-references
1. MAZAlib - basic image processing library. Contains a description of the implemented segmentation and filtering approaches: [mazalib](https://pypi.org/project/mazalib/)
2. PyFDMSS - a library to simulate single-phase flow on binary 3D pore geometries (Gerke, K. M., Vasilyev, R. V., Khirevich, S., Collins, D., Karsanina, M. V., Sizonenko, T. O., Korost, D.V., Lamontagne, S. & Mallants, D. (2018). Finite-difference method Stokes solver (FDMSS) for 3D pore geometries: Software development, validation and case studies. Computers & geosciences, 114, 41-58) [link](https://www.sciencedirect.com/science/article/abs/pii/S0098300417306234) : [pyfdmss](https://pypi.org/project/pyfdmss/)
