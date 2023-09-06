# OCR Transcriber

A script designed to convert PDF documents into text using Optical Character Recognition (OCR).

## Setup & Installation

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)
- [Poppler utility for Windows](https://github.com/oschwartz10612/poppler-windows#download)
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

To check the installation, the user can open a terminal and run the following Python commands:

```python
import pytesseract
print(pytesseract)
```

### Installation

#### Virtual Environment (optional)

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
    - Windows PowerShell: `.\venv\Scripts\Activate`
    - Bash: `source venv/bin/activate`

#### Dependencies

Install the required Python packages:

```bash
pip install pdf2image pytesseract opencv-python numpy
```

#### Poppler Utility

1. Download the Poppler for Windows binaries.
2. Extract and add the `bin` directory to the system's PATH.

#### Tesseract OCR

1. Download and install from the GitHub releases page.
2. Add Tesseract to the system's PATH or specify the path in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

To use the script, the user should run it and, when prompted, paste the full path to the PDF document. The script will process the document and output the transcribed text.

## Troubleshooting & Common Issues

### Poppler Not Found

**Error**: "Unable to get page count. Is poppler installed and in PATH?"

**Solution**: Ensure Poppler's `bin` directory is added to PATH. If a virtual environment is in use, ensure it's activated.

### Tesseract Not Found

**Error**: "tesseract is not installed or it's not in your PATH."

**Solution**: Ensure Tesseract is installed and its path is added to the system's PATH or specified in the script.

### PowerShell Script Execution Policy

**Error**: "File cannot be loaded because running scripts is disabled on this system."

**Solution**: Allow script execution by running `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell as Administrator.

## Current File Structure

```
ocr_pdf_populator/
├── src/
│   ├── __init__.py
│   ├── ocr_processing.py  # Functions related to OCR processing
│   ├── pattern_recognition.py  # Functions for extracting data using regex or other methods
│   ├── pdf_mapping.py  # Functions to map and fill fields in the destination PDF
│   └── utils/  # Utility functions, common constants, etc.
│       ├── __init__.py
│       └── helpers.py
│   ├── tests/  # Unit tests
│       ├── __init__.py
│       ├── test_ocr_processing.py
│       ├── test_pattern_recognition.py
│       └── test_pdf_mapping.py
│   ├── sample_pdfs/  # Sample PDFs for testing purposes
│       ├── input/
│       └── output/
│   ├── output/  # Directory where output PDFs are saved
│   └── main.py  # Main script that ties everything together
```

