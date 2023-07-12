from PIL import Image
from rembg import remove

def removebg():
    image = Image.open(input("Image Name: "))
    imagewbg = remove(image)
    imagewbg.save("modefied.png")

removebg()