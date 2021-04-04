'''
Smoothing and bluring techniques to an image
'''
import cv2 as cv

#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

cv.imshow('image',img)          

#kernel/Window -> Window drawn over a specific portion of image {Size of rows and columns is known as kernel size}

#1]Averaging                                 #Average of surrounding intensities alloted within that kernel size
average = cv.blur(img, (3,3))
cv.imshow('Averaged Image',average)

#2]Gaussian Blur                             #Avearage of product of weights allocated to those pizxel sets within that window {Less blurring as compared to average}
gauss = cv.GaussianBlur(img, (3,3), 0)       #Sigma func value just to mention deviation in x-axis
cv.imshow('Gaussian Image',gauss)

#3]Median Blurring                          #Finds median of surrounding pixels{More effective in removing background noise and effects}
median = cv.medianBlur(img, 3)               #Opencv detern=mines on its own with input literal
cv.imshow('Median',median)                    #Not at all meant for high kernel sizes than 3 ie 5 or 7

#4]Bilateral {#with low val looks similar to act img}                                 #Applies blurring but retains edges of image {When given larger values, gradually starts looking as medianblur}
bilateral = cv.bilateralFilter(img, 5, 15, 15)                #img, diameter, sigma colour and sigma space {larger sigma size value influences calculation since it covers region outside the kernel window}
cv.imshow('Bilateral Image', bilateral)

cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
