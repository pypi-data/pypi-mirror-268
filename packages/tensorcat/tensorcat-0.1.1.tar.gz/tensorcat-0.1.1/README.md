# TensorCat

This utility provides a unified interface to display an image/tensor/array in terminal, notebook and python debugger (pdb, ipdb). It utilizes the iTerm2 Inline Images Protocol to display an image inline. This protocol is also implemented by VSCode. To display image inside terminal, you need to use iTerm2 or the VSCode terminal with `terminal.integrated.enableImages` setting enabled.

## Usage

### Terminal (CLI)
```
python -m tensorcat.cli /path/to/img.png
tensorcat /path/to/img.png
```

### Python API (Can be used in Python Debugger or iPython Notebook)
```
from tensorcat import tensorcat
import torch
 
img = th.randn(4, 3, 32, 32)
tensorcat(img)
```
