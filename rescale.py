import cv2 as cv

img = cv.imread('Photos/image.jpg')      #to read an image of same directory 

#cv.imshow('image',img)          

'''Function to rescale video size'''
def rescaleFrame(frame, scale=0.75):
    #Applicable for images,videos,LiveVideo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Code to pass dimensions of rescale function to that image
'''
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
'''

cv.waitKey(0)

'''Change Resolution of video'''
def changeRes(width,height):
    #Only for Live Video
    capture.set(3,width)
    capture.set(4,height)                      #10 to change brightness

#code to read video
capture = cv.VideoCapture('Videos/new.mp4')       #can use integer value as 0,1,2,3 while using your webcameras else path of video
while True:
    isTrue, frame = capture.read()             #capture function reads video frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)                    #display each of video frame by frame
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):            #if letter d is pressed,we will break the loop
        break

capture.release()
cv.destroyAllWindows()                          #when we don't need it anymore.
