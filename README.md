OCR Transcriber
A script to convert PDF documents into text using OCR.

Setup & Installation
Prerequisites:
Python 3.x
Virtual environment (optional, but recommended)
Poppler utility for Windows
    https://github.com/oschwartz10612/poppler-windows#download
Tesseract OCR
    https://github.com/UB-Mannheim/tesseract/wiki
    Can check by running python (type "python" in powershell terminal and then "import pytesseract" and then "print(pytesseract)")
Installation:
Virtual Environment (optional):

Create a virtual environment: python -m venv venv
Activate it:
Windows PowerShell: .\venv\Scripts\Activate
Bash: source venv/bin/activate
Dependencies:

Install required Python packages:
Copy code
pip install pdf2image pytesseract opencv-python numpy
Poppler Utility:

Download Poppler for Windows binaries.
Extract and add the bin directory to your system's PATH.
Tesseract OCR:

Download and install from the GitHub releases page.
Add Tesseract to your system's PATH or specify the path in the script:
python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Usage:
Run the script and when prompted, paste the full path to your PDF document. The script will then process the document and output the transcribed text.

Troubleshooting & Common Issues:
Poppler Not Found:

Error: "Unable to get page count. Is poppler installed and in PATH?"
Solution: Ensure Poppler's bin directory is added to PATH. If using a virtual environment, make sure it's activated.
Tesseract Not Found:

Error: "tesseract is not installed or it's not in your PATH."
Solution: Make sure Tesseract is installed and its path is added to the system's PATH or specified in the script.
PowerShell Script Execution Policy:

Error: "File cannot be loaded because running scripts is disabled on this system."
Solution: Allow script execution by running: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser in PowerShell as Administrator.



CURRENT FILE STRUCTURE:

ocr_pdf_populator/
│
├── src/
│   ├── __init__.py
│   ├── ocr_processing.py   # Contains functions related to OCR processing
│   ├── pattern_recognition.py  # Contains functions for extracting data using regex or other methods
│   ├── pdf_mapping.py      # Contains functions to map and fill the fields in the destination PDF
│   └── utils/              # Utility functions, common constants, etc.
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                  # For unit tests
│   ├── __init__.py
│   ├── test_ocr_processing.py
│   ├── test_pattern_recognition.py
│   └── test_pdf_mapping.py
│
├── sample_pdfs/            # Sample PDFs for testing purposes
│   ├── input/
│   └── output/
│
├── output/                 # Directory where output PDFs are saved
│
└── main.py                 # Main script to tie everything together, taking user input or CLI args, etc.