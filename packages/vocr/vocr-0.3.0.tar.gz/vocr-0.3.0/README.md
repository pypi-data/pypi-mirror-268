# vocr - Vietnamese OCR


| | |
| :---: | :--- |
| Package Info | ![Supported Python Version](https://img.shields.io/pypi/pyversions/vocr?logo=python) <br> ![PyPI Version](https://img.shields.io/pypi/v/vocr?logo=pypi) ![License](https://img.shields.io/pypi/l/vocr?logo=github&color=blue) <br> ![Download per month](https://img.shields.io/pypi/dm/vocr) |
| Workflow | ![Test](https://github.com/AbsoluteWinter/vocr/actions/workflows/python-package.yml/badge.svg) <br> ![Release](https://github.com/AbsoluteWinter/vocr/actions/workflows/python-publish.yml/badge.svg) |
| Repo | ![Repo Size](https://img.shields.io/github/repo-size/AbsoluteWinter/vocr) |

<!-- ![Total Download](https://static.pepy.tech/badge/vocr) -->





## Prerequisite

- [Tesseract](https://github.com/UB-Mannheim/tesseract) installed and added to PATH


## Install

```
pip install vocr
```

## Usage

### Run in Terminal
```
vocr --help
```
```
Usage: vocr [OPTIONS] COMMAND [ARGS]...

  vocr's command line interface

Options:
  --help  Show this message and exit.

Commands:
  gui      Run vocr with GUI
  ocr      Performs OCR on file/directory
  version  Show current version
```

### Run in script
```python
from vocr import VietOCR
VietOCR(<path>).ocr()
```

## Supported file

- `.jpg`, `.jpeg`, `.png`

## LICENSE

MIT License