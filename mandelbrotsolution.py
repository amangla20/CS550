from PIL import Image, ImageFilter
import colorsys
import math
xa = 0
xb = 0
ya = 0
yb = 0
imgx, imgy = 512,512
image = Image.new("RGB", (imgx,imgy))
def mandelbrot_1():
	xa, xb = -0.5437, -0.5412
	ya, yb = 0.6137, 0.6162

	maxIt = 256 # max iteration

	for y in range(imgy):
		cy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			cx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			c = complex(cx, cy)
			z = 0
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = (i*-ya)/200
			g = i/128
			b = (i*yb)/100
			r,g,b = colorsys.hsv_to_rgb(r,g,b)
			image.putpixel((x,y),(int((r*5000)%256),int(g*256),int((b*1000)%256)))
	image.save("mandelbrotsol.png", "PNG")
	image.show()

mandelbrot_1()

image2 = Image.new("RGB", (imgx, imgy))
# A Mandelbrot with a Sobel filter found from code from this website: https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540
# I didn't copy the code exactly, as the original makes the outlines very grayish and dark, so I tweaked the code to make it my own and have a white gradient
def mandelbrot_2():
	xa, xb = -0.55, -0.54
	ya, yb = -0.505, -0.495
	imgx, imgy = 512, 512

	maxIt = 256
	for y in range(imgy):
		cy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			cx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			c = complex(cx, cy)
			z = 0
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = 255 - i
			g = 0
			b = 0
			image2.putpixel((x,y),(r,g,b))
	image2.show()
	image2.save("image2.png", "PNG")
	path = "image2.png"
	img = Image.open(path)
	for x in range(1, imgx-1):  # ignore the edge pixels for simplicity (1 to width-1)
		for y in range(1, imgy-1): # ignore edge pixels for simplicity (1 to height-1)

		    # initialise Gx to 0 and Gy to 0 for every pixel
		    Gx = 0
		    Gy = 0

		    # top left pixel
		    p = img.getpixel((x-1, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    # intensity ranges from 0 to 765 (255 * 3)
		    intensity = r + g + b

		    # accumulate the value into Gx, and Gy
		    Gx += -intensity
		    Gy += -intensity

		    # remaining left column
		    p = img.getpixel((x-1, y))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += -2 * (r + g + b)

		    p = img.getpixel((x-1, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += -(r + g + b)
		    Gy += (r + g + b)

		    # middle pixels
		    p = img.getpixel((x, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gy += -2 * (r + g + b)

		    p = img.getpixel((x, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gy += 2 * (r + g + b)

		    # right column
		    p = img.getpixel((x+1, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += (r + g + b)
		    Gy += -(r + g + b)

		    p = img.getpixel((x+1, y))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += 2 * (r + g + b)

		    p = img.getpixel((x+1, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += (r + g + b)
		    Gy += (r + g + b)

		    # calculate the length of the gradient (Pythagorean theorem)
		    length = math.sqrt((Gx * Gx) + (Gy * Gy))

		    # normalise the length of gradient to the range 0 to 255
		    length = length / 428 * 255

		    length = int(length)

		    # draw the length in the edge image
		    #newpixel = img.putpixel((length,length,length))
		    image2.putpixel((x,y),(length,length,length))
	image2.show()

mandelbrot_2()
