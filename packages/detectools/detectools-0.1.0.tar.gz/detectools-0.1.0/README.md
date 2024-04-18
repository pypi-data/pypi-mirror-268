<!--
<p align="center">
  <img src="https://github.com///raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  Detectools
</h1>


Torch overlay for trainning and inference processes for object detection & instance segmentation tasks. 
## 💪 Getting Started

Detectools provide a generalized data structure, trainning & inference process & evaluation metrics for different detection models inlcuded in library. Main goal is to be able to swithc from different detection models with minimal changes. To get an overview of main utilities of this library, take look at the [overall tutorial](./tutorials/overall.ipynb)


## 🚀 Installation

This package was develloped on python 3.11.

You can either clone the repo and install locally the library or install all from git (recommended).

#### Install from git:

This installation requires SSH access to both detectools & computervisiontools projects (UE APC).

```bash
pip install git+SSH://git@forgemia.inra.fr/ue-apc/librairies/python/detectools.git
```
#### Clone and local install (required for development):

```bash
git clone git@forgemia.inra.fr:ue-apc/librairies/python/detectools.git
cd detectools
pip install -e .
```

## 👐 Contributing

To ask for a modificatioins, bug fix or improvement proposal please add an issue on the project if you have access rights or contact Jordan Bernigaud Samatan (jordan.bernigaud-samatan@inrae.fr).

## Authors

* Lucas Bernigaud Samatan (lucas.bernigaudsamatan@inrae.fr)
* Jordan Bernigaud Samatan (jordan.bernigaud-samatan@inrae.fr)


### ⚖️ License

The code in this package is licensed under the MIT License.
