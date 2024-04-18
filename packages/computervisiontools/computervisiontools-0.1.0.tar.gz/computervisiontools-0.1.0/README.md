<!--
<p align="center">
  <img src="https://github.com///raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  ComputerVisionTools
</h1>


Basics of image processing and torch utilities for computer vision tasks.

## 💪 Getting Started

ComputerVisionTools contains general utilities for computer vision tasks as reading, writing images in torch format. Loading binary masks (segmentation tasks), set reproducibility and finally scripting models in torchscript. See tutorials for details.

## 🚀 Installation

This package was devloped on python 3.11.

You can either clone the repo and install locally the library or install all from git by copying only the requirements.txt file.

Cloning repository:

```shell
git clone git@forgemia.inra.fr:ue-apc/librairies/python/computervisiontools.git
cd computervisiontools
pip install .
```

Install from git (only if you don't want to modify the lib):

Copy contains of requirements_device.txt file you need in local file (requirements_local.txt) & install it. Then install library from git repository either with https of ssh if you have a key.

HTTPS:
```bash
pip install git+https://forgemia.inra.fr/ue-apc/librairies/python/computervisiontools.git
```
SSh
```bash
pip install git+ ssh://git@forgemia.inra.fr/ue-apc/librairies/python/computervisiontools.git
```

### Development Installation

To install in development mode, use the following:

```bash
git clone git@forgemia.inra.fr:ue-apc/librairies/python/computervisiontools.git
cd computervisiontools
pip install -e .
```

### ⚖️ License

The code in this package is licensed under the MIT License.

<!--
### 📖 Citation

Citation goes here!
-->
