import random as r
import math
from PIL import Image
imgx = 512
imgy = 512
image = Image.new("RGB",(imgx,imgy))

def mandelbrot():
	global r
	# initial z = (a,b)
	for d in range(imgy):
		for c in range(imgx):
			a = 0
			b = 0
			for x in range(2):
				# zsqr = (a^2-b^2,2*a*b)
				# z = zsqr + (-2+1*c/2,-2+1*d/2)
				# each c increases by 1/2 so it goes from -2 to 2
				# 1 try = red, 2 tries = green, and does not escape = blue
				a = ((a**2)-(b**2))+(-2+(c/(imgx/4)))
				b = (2*a*b)+(2-(d/(imgx/4)))
				if x == 0:
					if math.sqrt(a**2 + b**2) >= 2:
						image.putpixel((c,d),(255,0,0))
						break
				if x == 1:
					if math.sqrt(a**2 + b**2) >= 2:
						image.putpixel((c,d),(0,255,0))
						break
				# default pixel color is blue
				image.putpixel((c,d),(0,0,255))
				

mandelbrot()
image.save("mandelbrot.png", "PNG")