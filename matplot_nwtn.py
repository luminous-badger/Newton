#!/usr/bin/python

# Plots Newton fractal using matplotlib and a 2-d array.
# Does not use pylab.
# Need to plot for Y, for X as X,Y puts image vertical.
# Does not need X/Y Size or pixel. Nor rnum ...
# Prints X/Y Size for info only.
# pic_array is 2-d array for plotting image. Made up of rows of iter_array, a 1-d array of iter counts.
# Refreshed after each Y column is calculated.
# JM Wed 30 May 2018 15:51:45 BST
# Added print 'Created in {0:f} s'.format( dt ) and iter count multiples for better colour.
# JM Thu 31 May 2018 13:49:48 BST

import numpy as nm
import matplotlib.pyplot as plt
import cmath
import sys
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN   = -2.0
X_MAX   =  2.0
Y_MIN   = -2.0
Y_MAX   =  2.0
offset  =  0.01
epsilon = 0.001
maxiter = 50
calc_count = 0
rnum       = 1
pic_array  = []
lenlc      = len( colour_list )
lcmap      = 'summer'
ZPower     = 3.0

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

print 'X_size: ', X_SIZE ,' Y_size: ', Y_SIZE 

for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
	iter_array = []
	for X in nm.arange ( X_MIN, X_MAX, offset ):
                Z = complex ( X, Y )
                iter_count = 0

		while ( abs ( Z**ZPower - 1 ) > epsilon and iter_count < maxiter ):
			if ( Z ):
				Z =  Z - ( Z**ZPower - 1 ) / ( ZPower * Z**( ZPower - 1 ) ) 
                        iter_count = iter_count + 1
                        calc_count = calc_count + 1
                iter_array.append( iter_count * rnum )
	pic_array.append( iter_array )

dt = timer() - start

MsgText = 'Newton for Z^' + str( ZPower ) + ' ' + lcmap
print MsgText
print 'Created in {0:f} s'.format( dt )
print 'Calc: ', calc_count

fname = 'MPLT_Newton_' + str( lcmap ) + '.png'
print 'Fname:', fname	

plt.title( MsgText )

#plt.facecolor = 'white' 
plt.grid(True, color = 'w', linewidth = 2, linestyle = 'solid' ) 

fig = plt.gcf() # Required to save figure detail. Blank image otherwise.

plt.imshow( pic_array, extent=[ X_MIN, X_MAX, Y_MIN, Y_MAX ] )
#plt.set_cmap('afmhot')
plt.set_cmap( lcmap )
plt.show()
#plt.savefig( fname )

