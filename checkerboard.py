from PIL import Image

imgx = 512
imgy = 512
c = 0
image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	if y%64 == 0:
		c = 255 - c
	for x in range(imgx):
		# when x is divided by imgx/8, and its remainder is greater than imgx/4, then make red
		if x%64 == 0:
			c = 255 - c
		image.putpixel((x,y),(c,0,0))

image.save("checkboard.png","PNG")







