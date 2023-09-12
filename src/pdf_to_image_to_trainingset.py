from PIL import Image
import os
from ocr_processing import convert_pdf_to_images

# Path to the trainingset folder
trainingset_folder = os.path.abspath("./trainingset")

# Create a subfolder where the images will be saved
image_subfolder = os.path.join(trainingset_folder, "converted_images")
os.makedirs(image_subfolder, exist_ok=True)

# Iterate through each file in the folder
for filename in os.listdir(trainingset_folder):
    # Check if the file is a PDF
    if filename.endswith(".pdf"):
        # Construct the full path of the file
        full_file_path = os.path.join(trainingset_folder, filename)
        print(f"Converting file at path: {full_file_path}")

        # Save the current working directory
        original_working_directory = os.getcwd()

        # Change the working directory to the subfolder
        os.chdir(image_subfolder)

        # Call the function to convert the PDF to images and get the images list
        images = convert_pdf_to_images(full_file_path)

        # Save each image
        for i, image in enumerate(images):
            image_name = f"{filename}_image_{i+1}.png"
            image.save(image_name)
            print(f"Saved image {image_name}")

        # Change back to the original working directory
        os.chdir(original_working_directory)
