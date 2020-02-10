from PIL import Image
import pytesseract

# Download tesseract from https://github.com/UB-Mannheim/tesseract/wiki and install it.
# insted of my path copy your path where the Tesseract is installed and tesseract.exe exist

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Sasi\AppData\Local\Tesseract-OCR\tesseract.exe"
 
image = Image.open('test.png')
 
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
print(image_to_text)