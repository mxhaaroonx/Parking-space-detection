import cv2
import numpy as np
import pickle
import cvzone


c=cv2.VideoCapture('Parking footage.mp4')

#displaying the video fead by capturing each frames
while True:
    
    #looping the video
    if c.get(cv2.CAP_PROP_POS_FRAMES)== c.get(cv2.CAP_PROP_FRAME_COUNT): #current position and total no of frames in the video is compared
        c.set(cv2.CAP_PROP_POS_FRAMES,0) #resetting the frames to 0 once the video ends
    
    success, img= c.read()
    cv2.imshow("Image", img)
    cv2.waitKey(10)