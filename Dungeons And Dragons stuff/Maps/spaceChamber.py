#============================================================================
# Name        : SpaceChamber.py
# Author      : Antonius Torode
# Copyright   : This file can be used under the conditions of Antonius' 
#				 General Purpose License (AGPL).
# Created on  : May 21, 2018
# Description : This file is for tracking D&D rooms for the space chamber.
#============================================================================

import graphics
import random
import numpy as np

win=graphics.GraphWin("spaceChamber",500,500)
win.setBackground("white")
#col=graphics.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))

#defines the different stages.
main = False
downMiddle = False
upMiddle = False
	
def setFalse():
	'''
	Used for setting all variables to false.
	'''
	main = False
	downMiddle = False
	upMiddle = False

setFalse()

#defines variables for use with triangle.
triangle = []
trianglePos = []
vertices = [0,0,0]

def resetTriangle():
	'''
	Used for setting all triangle variables to default.
	'''
	triangle = []
	trianglePos = []
	vertices = [0,0,0]

#width of respective triangles/
w1 = 100
w2= 75
w3 = 25

a1 = np.sqrt(w1**2-w1**2/4)
a2 = np.sqrt(w2**2-w2**2/4)
a3 = np.sqrt(w3**2-w3**2/4)

#center of first triangle
c1x = 200
c1y = 200

#creates the colours for the triangles.
colour1 = graphics.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
colour2 = graphics.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))	
colour3 = graphics.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))	


def centeredTriangle(col,cx, cy, w, i): 
	'''
	Inputs are...
	Colour: col
	Center x position: cx
	Center y position: cy
	Width of triangle edge: w
	triangle index: i
	'''
	vertices[0] = graphics.Point(cx-w/2, cy-np.sqrt(w**2-w**2/4)/2)
	vertices[1] = graphics.Point(cx+w/2, cy-np.sqrt(w**2-w**2/4)/2)
	vertices[2] = graphics.Point(cx,     cy+np.sqrt(w**2-w**2/4)/2)
	
	triangle.append( graphics.Polygon(vertices) )      # Create the triangle
	triangle[i].setFill(col)
	triangle[i].draw(win)
	
def newCenterBottomRightX(s):
	'''
	Inputs are...
	Sector of triangle (2 or 3): s 
	'''
	if s == 2:
		return w1/2+w2/4
	if s == 3:
		return w2/2+w3/4
	return 0
	
def newCenterBottomY(s):
	'''
	Inputs are...
	Sector of triangle (2 or 3): s
	'''
	if s == 2:
		return a1/2-a2/2+np.sqrt(3*w2**2)/4
	if s == 3:
		return a2/2-a3/2+np.sqrt(3*w3**2)/4
	return 0
	
def newCenterBottomLeftX(s):
	'''
	Inputs are...
	Sector of triangle (2 or 3): s 
	'''
	if s == 2:
		return -w1/2-w2/4
	if s == 3:
		return -w2/2-w3/4
	return 0
	
def newCenterTopY(s):
	'''
	Sector of triangle (2 or 3): s 
	'''
	if s == 2:
		return a1/2+a2/2
	if s == 3:
		return a2/2+a3/2
	return 0
	
def main():
	'''
	Defines the main unchanged layout.
	'''
	centeredTriangle(colour1,c1x,c1y,w1,0)

	#sets the center coords for sector 2 triangles.
	c2xr = c1x+newCenterBottomRightX(2)
	c2yb = c1y-newCenterBottomY(2)
	c2xl = c1x+newCenterBottomLeftX(2)
	c2xt = c1x
	c2yt = c1y+newCenterTopY(2)

	#create sector 2 triangles.	
	centeredTriangle(colour2,c2xt,c2yt,w2,1)
	centeredTriangle(colour2,c2xr,c2yb,w2,2)
	centeredTriangle(colour2,c2xl,c2yb,w2,3)

	#sets the center coords for sector 3 triangles.
	c3ybb = c2yb-newCenterBottomY(3)
	c3xrr = c2xr+newCenterBottomRightX(3)
	c3xrl = c2xr+newCenterBottomLeftX(3)
	c3xrt = c2xr
	c3xlr = c2xl+newCenterBottomRightX(3)
	c3xll = c2xl+newCenterBottomLeftX(3)
	c3xlt = c2xl
	c3ylt = c2yb+newCenterTopY(3)

	#top triangles
	c3ytb = c2yt-newCenterBottomY(3)
	c3xtr = c2xt+newCenterBottomRightX(3)
	c3xtl = c2xt+newCenterBottomLeftX(3)
	c3xtt = c2xt
	c3ytt = c2yt+newCenterTopY(3)


	#create sector 3 triangles.
	centeredTriangle(colour3,c3xrr,c3ybb,w3,4)
	centeredTriangle(colour3,c3xrl,c3ybb,w3,5)
	centeredTriangle(colour3,c3xlr,c3ybb,w3,6)
	centeredTriangle(colour3,c3xll,c3ybb,w3,7)
	centeredTriangle(colour3,c3xlt,c3ylt,w3,8)
	centeredTriangle(colour3,c3xrt,c3ylt,w3,9)
	centeredTriangle(colour3,c3xtl,c3ytb,w3,10)
	centeredTriangle(colour3,c3xtr,c3ytb,w3,11)
	centeredTriangle(colour3,c3xtt,c3ytt,w3,12)

main()

input("Press ENTER to close.")