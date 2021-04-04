import cv2 as cv
#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

#cv.imshow('image',img)          

'''
#1]Converting image to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
'''
'''
#2]Blurring an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)        #to increase more blur quality
cv.imshow('Blur', blur)
cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
'''
'''
#3]Create Edge Cascade
#canny = cv.Canny(img, 125, 175)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)                            #to reduce the edges of background
cv.imshow('Canny', canny)
#cv.waitKey(0)
'''

'''
#4]Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated', dilated)
cv.waitKey(0)

#5]Eroding
#eroded = cv.dilate(canny, (3,3), iterations=1)
eroded = cv.dilate(canny, (7,7), iterations=3)               #to check similarity in dilated and eroded image; we get the edges back to our cascaded image
cv.imshow('Eroded', eroded)
cv.waitKey(0)
'''
'''
#6]Resize an image
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)                         #ignoring the aspect ratio;used if we are converting an image to a size ie lesser than the actual one
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR/CUBIC[Cubic is the smallest])                         #in case of enlarging and scaking an image
cv.imshow('Resized', resized)
cv.waitKey(0)
'''

#7]Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)
cv.waitKey(0)