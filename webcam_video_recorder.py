import numpy as np
import cv2
import os

# Standard dimensions dictionary
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# Video type dictionary
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def change_resolution(cap, width, height):
    """Change capture resolution"""
    cap.set(3, width)
    cap.set(4, height)

def get_dimensions(resolution='1080p'):
    """Get dimensions based on resolution"""
    width, height = STD_DIMENSIONS["480p"]
    if resolution in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[resolution]
    return width, height

def get_video_type(filename):
    """Get video type based on file extension"""
    _, ext = os.path.splitext(filename)
    return VIDEO_TYPE.get(ext.lower(), VIDEO_TYPE['avi'])

def main():
    """
    The main function for capturing video from a camera and saving it to a file.
    """
    filename = 'video.avi'
    frames_per_second = 24.0
    my_res = '720p'

    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(filename, get_video_type(filename), frames_per_second, get_dimensions(my_res))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
