<!--
<p align="center">
  <img src="https://github.com///raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  SegmenTools
</h1>


All classes and functions to train and use segmentation models with PyTorch.

## 💪 Getting Started

Segmentools provide low and high levels utilities to train, evaluate and deploy models. Low levels classes and functions are usefull develop new method while keeping data formats uniforms and high level classes allow to write scripts in a very concise and understable way. Be aware that Segmentools does not provide any segmentation model or loss function. Thise items have to be connected to segmentools pipelines respecting a few rules described in tutotrials.

## 🚀 Installation

This package was develloped on python 3.11.

You can either clone the repo and install locally the library or install all from git (recommended).

Install from git:

Copy contains of requirements_device.txt file you need in local file (requirements_local.txt) & install it. Then install library from git repository either with SSH (you need a SSH key to install dependencies like computervisiontools in both cases).

SSH:
```bash
pip install git+SSH://git@forgemia.inra.fr/ue-apc/librairies/python/segmentools.git
```

Cloning repository:

```shell
git clone git@forgemia.inra.fr:ue-apc/librairies/python/segmentools.git
cd segmentools
pip install .
```

### Development Installation

To install in development mode just add the -e option when installing with local repo:

```bash
git clone git@forgemia.inra.fr:ue-apc/librairies/python/segmentools.git
cd segmentools
pip install -e .
```

### ⚖️ License

The code in this package is licensed under the MIT License.
