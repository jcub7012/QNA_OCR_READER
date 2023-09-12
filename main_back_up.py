from src.ocr_processing import convert_pdf_to_images
from src.pattern_recognition import *
from src.roi_selector import get_rois
from src.text_processing import extract_text_from_images
import numpy as np
import os
import traceback  # Added for more detailed error tracing

def save_text_to_file(pdf_path, full_text):
    pdf_directory = os.path.dirname(pdf_path)
    filename = os.path.basename(pdf_path)
    text_file_path = os.path.join(pdf_directory, f"extracted_text_from_{filename}.txt")
    with open(text_file_path, 'w') as f:
        f.write(full_text)
    print(f"Debug: Text has been saved to {text_file_path}")
    return text_file_path

def main(pdf_path):
    try:
        print(f"Debug: Starting main function with pdf_path = {pdf_path}")

        images = convert_pdf_to_images(pdf_path)
        print(f"Debug: Number of images extracted = {len(images)}")
        if len(images) == 0:
            print("Debug: No images were extracted. Exiting.")
            return None

        images_np = [np.array(img) for img in images]
        print(f"Debug: Converted images to NumPy arrays.")

        all_rois = get_rois(images_np)
        print(f"Debug: All ROIs = {all_rois}")
        if not all_rois:
            print("Debug: No ROIs found. Exiting.")
            return None

        full_text = extract_text_from_images(images_np, all_rois)
        print(f"Debug: Full Text = {full_text}")
        if not full_text:
            print("Debug: No text extracted. Exiting.")
            return None

        text_file_path = save_text_to_file(pdf_path, full_text)
        print(f"Debug: Text file saved at {text_file_path}")

        extracted_details = {
            "Attorney Info": extract_attorney_info(full_text),
            "Address": extract_address(full_text),
            "Telephone": extract_telephone(full_text),
            "Email": extract_email(full_text),
            "Court": extract_court(full_text),
            "Petitioner": extract_petitioner(full_text),
            "Respondent": extract_respondent(full_text)
        }

        print("Debug: Extracted Details:")
        for key, value in extracted_details.items():
            print(f"{key}: {value}")

        return text_file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()  # This will print the error traceback, helping identify where the error occurred.