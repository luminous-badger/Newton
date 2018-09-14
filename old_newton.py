#!/usr/bin/python

# Attempt to do a Newton fractal in Python.
# JM Sun 21 Dec 2014 13:51:00 GMT

from pylab import imshow, show
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.0
X_MAX =  2.0
Y_MIN = -2.0
Y_MAX =  2.0
offset =  0.01
maxiter = 50
calc_count = 0
rnum = nm.random.randint( 1,100,1 )

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
X_SIZE += 1
Y_SIZE += 1

image = nm.zeros(( Y_SIZE, X_SIZE ), dtype = nm.uint8)

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( X, Y )
		iter = 0
		y_pixel += 1

		while ( abs ( Z**3 - 1 ) < 9 and iter < maxiter ):
			if ( Z ):
				#Z = ( Z**3 - 1 ) - ( ( Z**3 - 1 ) / ( 3 * Z**2 ) )
				Z =  ( 2 * Z**3 + 1 ) / ( 3 * Z**2 ) 

			iter = iter + 1
		
			calc_count = calc_count + 1  
		
		"""
		image[ y_pixel, x_pixel ] = iter + rnum
		"""
		if ( iter < maxiter ):
			image[ y_pixel, x_pixel ] = iter + rnum
		else:
			image[ y_pixel, x_pixel ] = 35
	x_pixel += 1

dt = timer() - start

print 'Newton and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
imshow(image)
show()

