# NeuroVisKit (alpha release)
## Package for Neural Modeling and Analysis of The Visual System
We connect the latest innovation in machine learning with neuroscientists to remove engineering from science.

1. See minimal.py for a minimal example of a modeling pipeline.
2. See tutorials for various tutorials and examples.

## Installation
Please make sure you have pytorch installed in order to fully utilize NeuroVisKit.

For installing a non-editable version run `pip install git+https://github.com/Yates-Lab/NeuroVisKit.git`

(append @\<branch-name\>) as needed.

For installing an editable version, clone and then run 

```
cd NeuroVisKit
pip install -e . -vvv
```

If imports don't work smoothly, go to VSCODE and search:
python -> pylance -> extra paths
and add the path to this dir
i.e. ~/Documents/NeuroVisKit