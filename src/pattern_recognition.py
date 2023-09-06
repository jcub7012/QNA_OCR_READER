import re
import cv2
import numpy as np
from pdf2image import convert_from_path
import pytesseract

def extract_case_no(text):
    print("Extracting case number...")
    match = re.search(r'CASE NUMBER:[\s]*?([\w\d]+)', text)
    case_no = match.group(1) if match else None
    print(f"Case number extracted: {case_no}")
    return case_no

def extract_petitioner(text):
    print("Extracting petitioner...")
    # Using [^\n]+ to capture all characters until the end of the line
    match = re.search(r'PLAINTIFF/PETITIONER: ([^\n]+)', text)
    petitioner = match.group(1).strip() if match else None
    print(f"Petitioner extracted: {petitioner}")
    return petitioner

def extract_respondent(text):
    print("Extracting respondent...")
    # Using [^\n]+ to capture all characters until the end of the line
    match = re.search(r'DEFENDANT/RESPONDENT: ([^\n]+)', text)
    respondent = match.group(1).strip() if match else None
    print(f"Respondent extracted: {respondent}")
    return respondent

def extract_attorney_info(text):
    print("Extracting attorney information...")
    match = re.search(r'ATTORNEY OR PARTY WITHOUT ATTORNEY \(Name, State Bar number\):\s*([^\n]+)', text)
    attorney_info = match.group(1).strip() if match else None
    print(f"Attorney information extracted: {attorney_info}")
    return attorney_info

def extract_address(text):
    print("Extracting address...")
    # This is a bit more complicated due to the multi-line nature of the address
    match = re.search(r'ATTORNEY OR PARTY WITHOUT ATTORNEY \(Name, State Bar number\):\s*[^\n]+\n([^\n]+)', text)
    address = match.group(1).strip() if match else None
    print(f"Address extracted: {address}")
    return address

def extract_telephone(text):
    print("Extracting telephone number...")
    match = re.search(r'TELEPHONE NO.:\s*([\d\s-]+)', text)
    telephone = match.group(1).strip() if match else None
    print(f"Telephone number extracted: {telephone}")
    return telephone

def extract_email(text):
    print("Extracting email address...")
    match = re.search(r'E-MAIL ADDRESS \(Optional\):\s*([\w\.-]+@[\w\.-]+)', text)
    email = match.group(1).strip() if match else None
    print(f"Email address extracted: {email}")
    return email

def extract_court(text):
    print("Extracting court information...")
    match = re.search(r'SUPERIOR COURT OF CALIFORNIA, COUNTY OF (.+)', text)
    court = match.group(1).strip() if match else None
    print(f"Court information extracted: {court}")
    return court

