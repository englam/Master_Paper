from PIL import Image
import pytesseract



im = Image.open('Captcha_dmongzbptd.jpg')

text = pytesseract.image_to_string(im)
print (text)


"""
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('Captcha_dmongzbptd.jpg') # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)"""