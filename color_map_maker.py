from __future__ import division
from PIL import Image
import numpy as np

scale = 100
size = (600, 600)
origin = (300, 300)

def hsv2rgb(h, s, v):
	h = float(h)
	s = float(s)
	v = float(v)
	h60 = h / 60.0
	h60f = np.floor(h60)
	hi = int(h60f) % 6
	f = h60 - h60f
	p = v * (1 - s)
	q = v * (1 - f * s)
	t = v * (1 - (1 - f) * s)
	r, g, b = 0, 0, 0
	if hi == 0: r, g, b = v, t, p
	elif hi == 1: r, g, b = q, v, p
	elif hi == 2: r, g, b = p, v, t
	elif hi == 3: r, g, b = p, q, v
	elif hi == 4: r, g, b = t, p, v
	elif hi == 5: r, g, b = v, p, q
	r, g, b = int(r * 255), int(g * 255), int(b * 255)
	return r, g, b

def sigmoid(n):
	return 1/(1+np.e**(n*-1))

def method(x, y):
	if x == 0:
		if y > 0:
			angle = 90
		elif y < 0:
			angle = 270
		else:
			angle = 0
	else:
		angle = np.arctan(y/x)*180/np.pi
	magnitude = np.sqrt(x**2+y**2)
	
	return hsv2rgb(angle, 1, sigmoid(magnitude))


color_map = Image.new("RGB", size, "black")
pixels = color_map.load()

for x in range(size[0]):
	for y in range(size[1]):
		pixels[x, y] = method( (x-origin[0])/scale, (y-origin[1])/scale )

color_map.show()
