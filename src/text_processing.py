import numpy as np
import pytesseract

def extract_text_from_images(images_np, all_rois):
    all_texts = []
    
    for idx, image in enumerate(images_np):
        rois_for_image = all_rois[idx]
        print(f"Debug: rois_for_image for image {idx + 1} = {rois_for_image}")

        if not rois_for_image:
            print(f"Skipping image {idx + 1} due to missing ROIs.")
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
                all_texts.append("=================== New Section ===================")
                
                # Debugging: Extracted text for each ROI
                print(f"Debug: Extracted Text for ROI {i + 1}: {text}")

            except Exception as e:
                print(f"Error processing ROI in image {idx + 1}: {e}")

    full_text = '\n'.join(all_texts)
    print(f"Debug: Full Text = {full_text}")  # Debugging: Full extracted text
    return full_text
