from src.ocr_processing import convert_pdf_to_images
from src.pattern_recognition import extract_case_no, extract_petitioner, extract_respondent
from src.roi_selector import get_rois
import numpy as np
import pytesseract

def main():
    try:
        # Debugging: Start of main function
        print("Debug: Starting main function.")

        # Step 1: Convert PDF to Images
        images = convert_pdf_to_images(r"C:\Users\User\Desktop\MORENO VALLEY\13-24 UUT COMPLAINT\MOV2 13-24 POS SUMMONS W ATTCHMNT 8.29.23.pdf")
        
        # Debugging: After PDF to Images
        print(f"Debug: Number of images extracted = {len(images)}")

        images_np = [np.array(img) for img in images]
        all_rois = get_rois(images_np)

        # Debugging: After getting all ROIs
        print(f"Debug: All ROIs = {all_rois}")

        all_texts = []
        
        for idx, image in enumerate(images_np):
            rois_for_image = all_rois[idx]
            print(f"Debug: rois_for_image for image {idx + 1} = {rois_for_image}")

            if not rois_for_image or len(rois_for_image) % 2 != 0:
                print(f"Skipping image {idx + 1} due to invalid ROIs.")
                continue

            for i in range(0, len(rois_for_image)):
                try:
                    (startX1, startY1), (startX2, startY2) = rois_for_image[i][0], rois_for_image[i][1]
                    print(f"Debug: point1 = ({startX1, startY1}), point2 = ({startX2, startY2})")

                    startX = int(min(startX1, startX2))
                    startY = int(min(startY1, startY2))
                    endX = int(max(startX1, startX2))
                    endY = int(max(startY1, startY2))
                    
                    roi_img = image[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi_img).strip()
                    all_texts.append(text)

                    # Add delimiter after each text block
                    all_texts.append("@@@DELIMITER@@@")
                    
                    # Debugging: Extracted text for each ROI
                    print(f"Debug: Extracted Text for ROI {i + 1}: {text}")

                except Exception as e:
                    print(f"Error processing ROI in image {idx + 1}: {e}")

            all_texts.append("@@@DELIMITER@@@")

        full_text = '\n'.join(all_texts)

        # Debugging: Full extracted text
        print(f"Debug: Full Text = {full_text}")

        case_no = extract_case_no(full_text)
        petitioner = extract_petitioner(full_text)
        respondent = extract_respondent(full_text)

        print(f"Extracted Details:\nCase No: {case_no}\nPetitioner: {petitioner}\nRespondent: {respondent}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
