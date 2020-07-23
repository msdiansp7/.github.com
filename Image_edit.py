#from PIL import Image,ImageEnha#nce
#import os

#img1=Image.open("Msdiansp.jpg")
#img1.save("Msdiansp.png")
#img1.show()
#imgsize=(250,250)
#img1.thumbnail(imgsize)
#img1.save("Msdiansp.jpg")
#img1.show()
#for item in os.listdir():
#    if item.endswith(".jpg"):
#        img1=Image.open(item)
#        filename,extension=os.path.splitext(item)
#        img1.save(f"{filename}1.pdf")
#        imgsize=(150,150)
#        img1.thumbnail (imgsize)
#        img1.save(item)
#from PIL import Image,ImageEnhance
#import os


#img1=Image.open("Msdiansp.jpg")
#enhancer=ImageEnhance.Sharpness(img1)
#enhancer.enhance(2).save("original.jpg")
#img1=Image.open("Msdiansp.jpg")
#enhancer=ImageEnhance.Color(img1)
#enhancer.enhance(0).save("bNw.jpg")
#enhancer.enhance(2).save("bNw.jpg")
#from PIL import Image,ImageEnhance
#import os

#img1=Image.open("Msdiansp.jpg")
#enhancer=ImageEnhance.Brightness (img1)
#enhancer.enhance(.7).save("brightness.jpg")
#from PIL import Image,ImageEnhance,ImageFilter
#import os

#img1=Image.open("Msdiansp.jpg")
#img1.filter(ImageFilter.GaussianBlur(0)).save("Blured.jpg")