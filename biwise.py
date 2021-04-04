import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)                 #img, center, radius, color, thickness

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


#Bitwise And                                               -->Intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise and', bitwise_and)                                     #Considers both the images and takes the intersection

#Bitwise Or                                               -->Non intersecting & intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise Or', bitwise_or)                                        #Put img 1 over 2 we get the resultant image

#Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#Bitwise NOT                                                       --> Converts black to white and white to black {Only one image to be passed}
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)


cv.waitKey(0)


