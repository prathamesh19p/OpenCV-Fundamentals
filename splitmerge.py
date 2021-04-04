import cv2 as cv
#import matplotlib.pyplot as plt
import numpy as np
#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

cv.imshow('image',img)  

blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,r,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merged = cv.merge([b,g,r])
merged = cv.merge([b,g,r])                     #if wrote blue , green , red gives an error
cv.imshow('Merged Image',merged)

cv.waitKey(0)