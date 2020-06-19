from PIL import Image
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
img = Image.open( 'temp.png' )
img.load()

new_size = tuple( 2 * x for x in img.size )
img = img.resize( new_size, Image.ANTIALIAS )
img.save('temp.png')
img = Image.open('temp.png')
img.load()
print( pytesseract.image_to_string( img ) )
