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
		r = (i*-ya)/200
		g = i/256
		b = (i*yb)/100
		r,g,b = colorsys.hsv_to_rgb(r,g,b)
		image.putpixel((x,y),(int((r*5000)%256),int(g*256),int((b*10000)%256)))

image.show()
image.save("mandelbrotsol.png", "PNG")