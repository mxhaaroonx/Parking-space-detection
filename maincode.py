import cv2
import numpy as np
import pickle
import cvzone


c=cv2.VideoCapture('Park lot footage.mp4')

with open("Carpos", "rb") as file:
    pos=pickle.load(file)

width, height= 107, 48

def check():
    for p in pos:
        x,y = p
        crop=img[y:y+height, x:x+width] #crops each block of parking space
        cv2.imshow("Croppedvideo",crop) #shows each cropped video
        
#displaying the video feed by capturing each frames
while True:
    
    #looping the video
    if c.get(cv2.CAP_PROP_POS_FRAMES)== c.get(cv2.CAP_PROP_FRAME_COUNT): #current position and total no of frames in the video is compared
        c.set(cv2.CAP_PROP_POS_FRAMES,0) #resetting the frames to 0 once the video ends
    success, img= c.read()
    
    grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converting it to gray image since gray images work accurately for object detection
    blur=cv2.GaussianBlur(grayimg, (3,3),1) #smoothing out the edges
    #converting to binary image
    imgThres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    check()
    for p in pos:
        cv2.rectangle(img,p,(p[0]+width,p[1]+height),(255,0,0), 2)
    cv2.imshow("Image thres", imgThres)
    cv2.waitKey(10)