from pdf2image import convert_from_path
import pytesseract
import cv2  # Don't forget to import OpenCV

def convert_pdf_to_images(pdf_path):
    """
    Convert the provided PDF to a list of images.

    Args:
        pdf_path (str): Path to the input PDF file.

    Returns:
        list: A list of images extracted from the PDF.
    """
    
    # Configure paths for poppler
    poppler_path = r"C:\\Program Files\\poppler-23.08.0\\Library\\bin"

    # Convert PDF to list of images
    print("Starting PDF conversion...")
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    print("Conversion completed.")
    print(f"Extracted {len(images)} images from the PDF.")

    return images

def ocr_with_preprocessing(images_np, rois):
    """
    Perform OCR with preprocessing steps.

    Args:
        images_np (list): List of NumPy arrays representing images.
        rois (list): List of ROIs to extract from each image.

    Returns:
        list: List of extracted text from each ROI in each image.
    """

    # Your existing OCR and ROI extraction logic
    for i, img in enumerate(images_np):
        rois_for_image = rois[i]
        for j in range(0, len(rois_for_image), 2):
            # Extracting ROI from image (example)
            point1, point2 = rois_for_image[j], rois_for_image[j+1]
            roi_img = img[point1[1]:point2[1], point1[0]:point2[0]]

            # Preprocessing steps
            # For example, using morphological closing
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            processed_img = cv2.morphologyEx(roi_img, cv2.MORPH_CLOSE, kernel)
            
            # Then, OCR on processed image
            text = pytesseract.image_to_string(processed_img).strip()
            
            # Append the extracted text to your text list or perform other tasks

    # Return your list of text or other desired outputs