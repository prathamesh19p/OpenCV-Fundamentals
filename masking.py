'''
Masking allows to focus on certain part of image which we are interested of 
{For example :- Image of a person and we focus on only face is known as masking}
'''
import cv2 as cv
import numpy as np
#Code to read images

img = cv.imread('Photos/image2.jpg')      #to read an image of same directory 

#img = cv.imread('Photos/image2.jpg')

#cv.imshow('image',img)          

#if instead of {:2} we write actual dim like (300,300) then it raises an errror
blank = np.zeros(img.shape[:2], dtype='uint8')             #dimensions of mask must be of same size should be exactly equal to that of img else it wont work

cv.imshow('Blank Image',blank)

#mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100 , img.shape[0]//2 + 100), 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 100 , img.shape[0]//2 + 100), 100, 255, -1)

#cv.imshow('Masked Image', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)

cv.imshow('Weird Shape',weird_shape)

#masked = cv.bitwise_and(img,img,mask=mask)


masked = cv.bitwise_and(img,img,mask=weird_shape)

#cv.imshow('Masked Image', masked)
cv.imshow('Weird Shaped Masked Image', masked)
cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
