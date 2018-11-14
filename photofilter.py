from PIL import Image
import math
import colorsys

path = "healey_1.jpeg" # Your image path 
img = Image.open(path)
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
        g = (g/500)**2
        b = (b/300)

        r,g,b = colorsys.hsv_to_rgb(r,g,b)

        newimg.putpixel((x,y),((int(r*256)),(int(g*256)),(int(b*256))))
newimg.show()
newimg.save("filteredphoto.png", "PNG")
# path = "filteredphoto.png"
# img1 = Image.open(path)
# imgx, imgy = img.size
# img2 = Image.new("RGB", (imgx, imgy))

# for x in range(1,imgx-1):
# 	for y in range(1, imgy-1):
# 		p = img.getpixel((x,y))
# 		r = p[0]
# 		g = p[1]
# 		b = p[2]

#         r = x/64
#         g = (g/500)**2
#         b = (b/300)

#         r,g,b = colorsys.hsv_to_rgb(r,g,b)

#         img2.putpixel((x,y),((int(r*256)),(int(g*256)),(int(b*256))))

# img2.show()
