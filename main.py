from src.ocr_processing import convert_pdf_to_images
from src.pattern_recognition import *
from src.roi_selector import get_rois
from src.text_processing import extract_text_from_images
import numpy as np
import os  # Add this import for file operations

def save_text_to_file(pdf_path, full_text):
    pdf_directory = os.path.dirname(pdf_path)
    text_file_path = os.path.join(pdf_directory, "extracted_text.txt")
    with open(text_file_path, 'w') as f:
        f.write(full_text)
    print(f"Text has been saved to {text_file_path}")
    return text_file_path  # Add this line to return the path of the saved text file

def main(pdf_path):
    try:
        print("Debug: Starting main function.")

        # Removed hardcoded pdf_path
        images = convert_pdf_to_images(pdf_path)
        print(f"Debug: Number of images extracted = {len(images)}")

        images_np = [np.array(img) for img in images]
        all_rois = get_rois(images_np)
        print(f"Debug: All ROIs = {all_rois}")

        full_text = extract_text_from_images(images_np, all_rois)
        print(f"Debug: Full Text = {full_text}")

        text_file_path = save_text_to_file(pdf_path, full_text)  # Capturing the returned text file path

        extracted_details = {
            "Attorney Info": extract_attorney_info(full_text),
            "Address": extract_address(full_text),
            "Telephone": extract_telephone(full_text),
            "Email": extract_email(full_text),
            "Court": extract_court(full_text),
            "Petitioner": extract_petitioner(full_text),
            "Respondent": extract_respondent(full_text)
        }

        print("Extracted Details:")
        for key, value in extracted_details.items():
            print(f"{key}: {value}")

        return text_file_path  # Add this line to return the path of the saved text file

    except Exception as e:
        print(f"An error occurred: {e}")
