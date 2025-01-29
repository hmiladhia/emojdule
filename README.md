# 🐍 emojdule
![PyPI](https://img.shields.io/pypi/v/emojdule)
![PyPI - License](https://img.shields.io/pypi/l/emojdule)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/emojdule)
![Tests](https://github.com/hmiladhia/emojdule/actions/workflows/quality.yaml/badge.svg)

Import Python modules with snake emoji extension!

![Screenshot](assets/screen.png)

## Installation

```bash
pip install emojdule
```

## Usage
Once you have installed emojdule in your venv, there is nothing else to do, you can just import your modules like usual.

You can see an example [here](./example/main.py)

```
example
├── package
│ ├── subpackage
│ │ ├── __init__.🐍
│ │ └── submodule.🐍
│ ├── __init__.🐍
│ └── module.🐍
└── main.py
```

```python
# main.py

from package.module import hello

hello()  # Hello from snake module! 🐍
```
