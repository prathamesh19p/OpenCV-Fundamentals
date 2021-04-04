'''
Computing Histograms
'''
#Helps to analyze pixel intensities in an image
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#Code to read images
img = cv.imread('Photos/image.jpg')      #to read an image of same directory 
#img = cv.imread('Photos/image2.jpg')

cv.imshow('image',img)          
blank = np.zeros(img.shape[:2], dtype='uint8') 
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked Image', mask)
#cv.imshow('Masked Image', circle)

#Grayscale histograms
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])           #images , channels , mask, histSize, range
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])           #when mask is included

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim(0,256)
plt.show()

cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
'''

#RGB color image histogram

plt.figure()
plt.title('BGR Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked Image', mask)
'''

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray, gray, mask=mask)

colors = ('b','g','r')
for i,col in enumerate(colors):
    #hist = cv.calcHist([img], [i], None, [256], [0,256])
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)

plt.show()

cv.waitKey(0)