#python program to extract text from the attached image

import pytesseract as tess                           #importing modules
from PIL import Image


img = Image.open("C:/Users/rosha/Desktop/demo.jpg")  #loading images

text = tess.image_to_string(img)                     #converting image to string

print(text)