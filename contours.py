#Boundary of object with not equal as edges mathematically
import cv2 as cv
import numpy as np
#Code to read images

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

#cv.imshow('image',img)          

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny edges',canny)


ret, thresh = cv.threshold(gray, 125,  255, cv.THRESH_BINARY)
cv.imshow('Threshed Image', thresh)


#RETR_TREE -> heirarchical contours ; RETR_LIST ->all contours; RETR_EXTERNAL for external contours
contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)        #CHAIN_APPROX is to note how we want to approx our contours {Simple:compresses all contours to endpoints}
#print(f'(len(contours)) contour(s) found!!')
print(len(contours))                  #Blurring an image reduces value of contours tremendously


cv.drawContours(blank, contours, -1, (0,0,255), thickness=2)
cv.imshow('Countours Drawn', blank)                         #to compare with canny, comment threshold waala part and pass in canny to main function inplace of thresh
cv.waitKey(0)