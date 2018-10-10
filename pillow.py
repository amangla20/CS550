from PIL import Image

imgx = 512
imgy = 512
c = 0
r = 0
b = 0
image = Image.new("RGB",(imgx, imgy))
# do 8 panels of going from black to red (like the example shown in class)
# 512 is the width, 512/8 = 64
# 64 pixels going from black to red for each "panel"
# range(256) for going from 0 to 255 in the rgb color scheme (255, 0, 0) is red
# 256/64 = 4 --> that means that it increments 4 shades per pixels for each panel
# image.putpixel((0,0),(255,0,0))
for y in range(imgx):
	for x in range(imgy):
			image.putpixel((x,y),(c,0,0))
			c += 4
			if c == 256:
				# reset c to 0 once it reaches (255,0,0)
				c = 0

image.save("demo_image.png", "PNG")

image2 = Image.new("RGB",(imgx, imgy))
# cool image
for x in range(512):
	for y in range(512):
		image2.putpixel((x,y),(r,0,b))
		r += 1
		if r == 256:
			r = 0
			b += 1

image2.save("second_image.png", "PNG")
			




