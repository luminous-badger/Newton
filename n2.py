#!/usr/bin/python

# From: http://23ars.blogspot.co.uk/2013/07/fractals-in-python-using-newton-raphson.html

from PIL import Image
import math
imgx = 600
imgy = 600
image = Image.new("RGB", (imgx, imgy))
 
# drawing area
x0 = -1.0
x1 = 1.0
y0 = -1.0
y1 = 1.0
name=raw_input("Enter the name of the picture:")
name=name+".png"
maxIt = 50 # max iterations allowed
ds = 0.002e-1# step size for numerical derivative
eps = 5e-19 # max error allowed
 
# put a complex function here to generate a fractal
def f(z):
    return z * z * z - 1.0
  
 
# draw the fractal
for y in range(imgy):
    zy = y * (y1 - y0) / (imgy - 1) + y0
    for x in range(imgx):
        zx = x * (x1 - x0) / (imgx - 1) + x0
        z = complex(zx, zy)
        for i in range(maxIt):
            #calculates derivative
            dz = (f(z + complex(ds, ds)) - f(z)) / complex(ds, ds)
            z0 = z - f(z) / dz # Newton iteration
            if abs(z0 - z) < eps: # stop when close enough to any root
                break
            z = z0
	image.putpixel((x, y), (i % 8 * 16, i % 4 * 32,i % 2 * 64))        
	
 
image.save(name, "PNG")
