# Anjali Mangla
# Image Filter Class Activity
# Sources: https://pythontic.com/image-processing/pillow/blend (blending)
from PIL import Image
import math
import colorsys

path1 = input("What is the name of the image you would like to filter? ")
# path = "healey_1.jpeg" # Your image path 
img = Image.open(path1)
imgx, imgy = img.size
newimg = Image.new("RGB", (imgx, imgy))
for x in range(1, imgx-1):  # ignore the edge pixels for simplicity (1 to width-1)
    for y in range(1, imgy-1): # ignore edge pixels for simplicity (1 to height-1)

        # # initialise Gx to 0 and Gy to 0 for every pixel
        # Gx = 0
        # Gy = 0

        # top left pixel
        p = img.getpixel((x,y))
        r = p[0]
        g = p[1]
        b = p[2]

        r = y/64
        g = (g/500)
        b = (b/300)

        r,g,b = colorsys.hsv_to_rgb(r,g,b)

        newimg.putpixel((x,y),((int(r*256)),(int(g*256)),(int(b*256))))
#newimg.show()
newimg.save("horizontallines.png", "PNG")
path2 = "horizontallines.png"
img1 = Image.open(path2)
imgx, imgy = img.size
img2 = Image.new("RGB", (imgx, imgy))

for y in range(1, imgy-1):
	for x in range(1, imgx-1):
		p = img.getpixel((x,y))
		r = p[0]
		g = p[1]
		b = p[2]

		r = x/64
		g = (g/500)
		b = (b/300)

		r,g,b = colorsys.hsv_to_rgb(r,g,b)

		img2.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))

#img2.show()
img2.save("verticallines.png", "PNG")

path3 = "verticallines.png"
# Take two images for blending them together   
image1 = Image.open(path2)
image2 = Image.open(path3)

# Make sure images got an alpha channel
image3 = image1.convert("RGBA")
image4 = image2.convert("RGBA")

# alpha-blend the images with varying values of alpha
alphaBlended = Image.blend(image3, image4, alpha=.6)

# Display the alpha-blended images
alphaBlended.show()

alphaBlended.save("filteredphoto.png")
