import cv2 as cv

#Code to read images
img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

cv.imshow('image',img)          

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

#Simple thresholding
#threshold,thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)              {Greater the value, more is whiteness in the image}
threshold,thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

cv.imshow('Threshold Image', thresh)

#Inverse Thresholded Image
threshold,thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)

cv.imshow('Inverse Threshold Image', thresh_inv)

#Adaptive Thresholding
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) #src img, maxValue, adaptiveMethod, thresholdType, blksize, c{value ie subtracted from mean}
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 0) #src img, maxValue, adaptiveMethod, thresholdType, blksize, c{value ie subtracted from mean}
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3) #src img, maxValue, adaptiveMethod, thresholdType, blksize, c{value ie subtracted from mean}
cv.imshow('Adaptive Thresholding',adaptive_thresh)

cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
