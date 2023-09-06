import os

def save_text_to_file(pdf_path, full_text):
    """
    Save the given text to a new text file in the same directory as the given PDF.
    
    :param pdf_path: The path to the PDF file.
    :param full_text: The full text to save.
    """
    # Extract the directory where the PDF is stored
    pdf_directory = os.path.dirname(pdf_path)
    
    # Create a new text file path
    text_file_path = os.path.join(pdf_directory, "extracted_text.txt")
    
    # Write the full_text to the new text file
    with open(text_file_path, 'w') as f:
        f.write(full_text)
    
    print(f"Text has been saved to {text_file_path}")

# Example usage:
pdf_path = "path/to/your/pdf/file.pdf"
full_text = "Your full OCR scanned text here..."
save_text_to_file(pdf_path, full_text)
