import cv2 as cv
import numpy as np
#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

#cv.imshow('image',img)          

'''
#1]Translation  #shifting image up,down,left,right (-x -> left ; -y -> up ; +x -> right ; +y -> down)
def translate(img, x, y):                  #x,y are pixels to be shifted in resp axis
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img , 100, 100)
cv.imshow('Translated', translated)
'''
'''
#2]Rotation #rotating an image by an angle
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:                     #rotating abt the center
        rotPoint = (width//2,height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width,height)

        return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)                #if angle is negative,rotates anticlockwise
#cv.imshow('Rotated', rotated)
rotated_rotated = rotate(rotated, -45)
cv.imshow("Rotated Image", rotated_rotated)
'''
'''
#3]Resizing an image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)
'''
'''
#4]Flipping an image
flip = cv.flip(img, 0)             #0 -> x-axis; 1-> y-axis; -1 -> both x & y axis
cv.imshow('Flipped Image', flip)
'''
'''
#5] Cropping an image
cropped = img[200:400, 300:400]
cv.imshow('Cropped Image', cropped)
'''


cv.waitKey(0)

