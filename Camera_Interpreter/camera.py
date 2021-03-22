# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

from enum import Enum



class object_states(Enum):
    pencil = "pencil grip configuration"
    cup = "cup grip configuration"

#https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/
#https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/
#https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/


class camera_interface():
    """Provides the main interface for using the camera and determining the grip we need to be in."""
    # https://www.hackster.io/gatoninja236/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b

    def __init__(self):
        # set up camera object
        self.cap = cv2.VideoCapture(0)

        # QR code detection object
        self.detector = cv2.QRCodeDetector()
        
    def read_cam(self):
        # get the image
        _, img = self.cap.read()
        # get bounding box coords and data
        data, bbox, _ = self.detector.detectAndDecode(img)
        #return the information we got from the camera
        return data, bbox, img

    def read_cam_display_out(self):
        #Call the standard method to get the qr data / bounding box
        data, bbox = self.read_cam()
        # if there is a bounding box, draw one, along with the data
        if(bbox is not None):
            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                        0, 255), thickness=2)
            cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            if data:
                print("data found: ", data)
        # display the image preview
        cv2.imshow("code detector", img)

    def end_camera_session(self):
        #Release the camera object
        self.cap.release()
        #Destroy all displayed windows
        cv2.destroyAllWindows()