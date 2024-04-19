# vocr
 
Vietnamese OCR

## Prerequisite

- [Tesseract](https://github.com/UB-Mannheim/tesseract) installed and added to PATH

- Clone this project

## Install

```
pip install vocr
```

## Usage:

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
  ocr      Performs OCR on file/directory
  version  Show current version
```

### Run in script
```python
from vocr import VietOCR
VietOCR(<path>).ocr()
```

## LICENSE

MIT License