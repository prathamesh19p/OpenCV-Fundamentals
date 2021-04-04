#To draw on images

import cv2 as cv
import pandas as pd
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')  #wwidth,height and number of colourchannels

#cv.imshow('Blank', blank)

#img = cv.imread('Photos/image.jpg')
#cv.imshow('Image',img)

#Paint the image a certain color
#blank[:] = 255,0,0             #rgb component distribuition
#blank[200:300, 300:400] = 0,0,255      #range of pixels
#cv.imshow('Red', blank)

#Draw a rectangle
#cv.rectangle(blank, (0,0), (50,250), (0,255,0), thickness=2)  #width,height,pixels and thickness with color of rect

#cv.rectangle(blank, (0,0), (50,250), (0,255,0), thickness=cv.FILLED)  #width,height,pixels and thickness with color of rect - cv.Filled fills color in rect

'''
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0))
cv.imshow('Rectangle', blank)
'''
'''
#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) #size,parameter,radius in pixels and color,thickness
cv.imshow('Circle', blank)
'''
'''
#Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('line', blank)
'''

#Write text on an image

#cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)      #properties to display the text like font pos color scale/size etc.
cv.putText(blank, 'Hello my name is Soham', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)      #properties to display the text like font pos color scale/size etc.

cv.imshow('Text', blank)
cv.waitKey(0)