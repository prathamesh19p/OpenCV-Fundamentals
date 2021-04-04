import cv2 as cv

#Code to read images
'''
img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

cv.imshow('image',img)          

cv.waitKey(0)                   #keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
'''
'''
#code to read video
capture = cv.VideoCapture('Videos/new.mp4')       #can use integer value as 0,1,2,3 while using your webcameras else path of video
while True:
    isTrue, frame = capture.read()             #capture function reads video frame by frame
    cv.imshow('Video', frame)                    #display each of video frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'):            #if letter d is pressed,we will break the loop
        break

capture.release()
cv.destroyAllWindows()                          #when we don't need it anymore.
'''
 #File "read.py", line 14, in <module>
 #   cv.imshow('Video', frame)
#cv2.error: OpenCV(4.5.1) C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-r2ue8w6k\opencv\modules\highgui\src\window.cpp:376: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
##This error occurs when opencv doesn't find frames of this video further..

'''Resizing and Recalling'''



