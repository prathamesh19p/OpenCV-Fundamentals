#Note:- gray scale to lab is not a direct conversion possible , we first have to convert to rgb or
import cv2 as cv
import matplotlib.pyplot as plt
#import numpy as np
#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

cv.imshow('image',img)  

#plt.imshow(img)
#plt.show()

'''
#1]BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
'''
'''
#2]BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Hsv',hsv)
'''
'''
#3]BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)
'''
'''
#4]BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()
'''
'''
#5]HSV to BGR                                   #similarly we can try for lab -> bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV Conv image',hsv_bgr)
'''

cv.waitKey(0)