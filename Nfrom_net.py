#!/usr/bin/python

from PIL import Image
#size of image
imgx = 600
imgy = 400
#make image buffer
image = Image.new("RGB", (imgx, imgy))

# area of fractal
xa = -2.0
xb = 2.0
ya = -2.0
yb = 2.0

#define constants
max_iterations = 10 # max iterations allowed
step_derivat = 0.002e-1 # step size for numerical derivative
error = 5e-19 # max error allowed

# function will generate the newton fractal
def f(z): return z * z  + complex(-0.31,0.031)

# draw derivate fractal for each y and x 
for y in range(imgy):
 zy = y * (yb - ya)/(imgy - 1) + ya
 for x in range(imgx):
  zx = x * (xb - xa)/(imgx - 1) + xa
  z = complex(zx, zy)
  for i in range(max_iterations):
   # make complex numerical derivative
   dz = (f(z + complex(step_derivat, step_derivat)) - f(z))/complex(step_derivat,step_derivat)
 # Newton iteration see wikipedia   
   z0 = z - f(z)/dz 
   # stop to the error 
   if abs(z0 - z) < error: 
    break
   z = z0
  #I use modulo operation expression to do RGB colors of the pixels 
  image.putpixel((x, y), (i % 8 * 16, i % 4 * 32,i % 2 * 64))
  
#save the result 
image.save("nfractal.png", "PNG")

