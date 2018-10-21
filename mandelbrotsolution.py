from PIL import Image
import colorsys

xa, xb = -0.5435, -0.541
ya, yb = 0.6135, 0.616

imgx, imgy = 512,512

maxIt = 256 # max iteration

image = Image.new("RGB", (imgx,imgy))

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
		r = int(256 - i)
		g = int(r%i)
		b = int((i*50)%256)
		image.putpixel((x,y),(r,g,b))

image.show()
image.save("mandelbrotsol.png")