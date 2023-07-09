from PIL import Image
from rembg import remove

#Open image
img = Image.open(input("Filename: "))
#Removing background
imgwbg = remove(img)
#Saving image
imgwbg.save("image_without_background.png")