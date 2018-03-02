from __future__ import division
from PIL import Image
from numpy import *
import sys

# Vars
scale = 100
size = (600, 600)
origin = (300, 300)

# Function
expression = raw_input("f(z) = ")
def function(z):
	return eval(expression)

# In-fill functions

def stripe(x, y):
	val = x + y*size[0]
	if mod(val, size[0]/5 + 0.2) < size[0]/10:
		return (0, 0, 100)
	else:
		return (255, 255, 255)

def solid_black(x, y):
	return (0, 0, 0)

# Getting Color Map
color_map_name = raw_input("Color Map: ")
color_map = Image.open(color_map_name)
map_pixels = color_map.load()

# Making Image
output = Image.new("RGB", size, "black")
output_pixels = output.load()

for x in range(size[0]):
	for y in range(size[1]):
		try:
			val = function( (x-origin[0])/scale + (y-origin[1])*1j/scale )
		except:
			output_pixels[x, y] = (255, 255, 255)
			break
		try:
			output_pixels[x, y] = map_pixels[ val.real*scale + origin[0], val.imag*scale + origin[1] ]
		except:
			output_pixels[x, y] = solid_black(x, y)
output.show()
