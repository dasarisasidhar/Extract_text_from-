from PIL import Image
import pytesseract

# Download tesseract from https://github.com/UB-Mannheim/tesseract/wiki and install it.
# Give the Tesseract installed path where tesseract.exe is exist

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Sasi\AppData\Local\Tesseract-OCR\tesseract.exe"
 
image = Image.open('test.png')
 
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
print(image_to_text)
