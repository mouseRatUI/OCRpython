import os
import pytesseract
from PIL import Image

# Set path to Tesseract executable (if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set path to folder containing images
folder_path = r"D:\pythonOCRtest\folderForPictures"

# Loop through files in folder
for file_name in os.listdir(folder_path):
    # Check if file is an image
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        # Load image using PIL
        image_path = os.path.join(folder_path, file_name)
        image = Image.open(image_path)

        # Convert image to grayscale
        image = image.convert('L')

        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image)

        # Print recognized text
        print(f"File name: {file_name}\nText:\n{text}\n")
