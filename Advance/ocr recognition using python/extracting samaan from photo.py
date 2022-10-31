from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\LENOVO\Desktop\New folder\noPlate_0.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])
d=text[:-1]
f=open('NUMBER_PLATE_TEXT.txt','w+')
f.write(d)
f.close()
