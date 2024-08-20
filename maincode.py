import cv2
import numpy as np
import pickle
import cvzone


c=cv2.VideoCapture('Park lot footage.mp4')

with open("Carpos", "rb") as file:
    pos=pickle.load(file)

width, height= 107, 48

def check(imgpro):
    for p in pos:
        x,y = p
        crop=imgpro[y:y+height, x:x+width] #crops each block of parking space
        #cv2.imshow("Croppedvideo",crop) #shows each cropped video
        count=cv2.countNonZero(crop) #counting the amount of white pixels in each cropped image 
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,thickness=2, offset=0) #used to display the no of white pixels 
        if count <1200:
            color=(0,255,0)
            thick=5
        else:
            color=(0,0,255)
            thick=3
        
        cv2.rectangle(img,p,(p[0]+width,p[1]+height),color, thick)

#displaying the video feed 
while True:
    
    #looping the video
    if c.get(cv2.CAP_PROP_POS_FRAMES)== c.get(cv2.CAP_PROP_FRAME_COUNT): #current position and total no of frames in the video is compared
        c.set(cv2.CAP_PROP_POS_FRAMES,0) #resetting the frames to 0 once the video ends
    success, img= c.read()
    
    grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converting it to gray image since gray images work accurately for object detection
    blur=cv2.GaussianBlur(grayimg, (3,3),1) #smoothing out the edges
    
    imgThres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16) #gives a salt and pepper sort of image to identify cars
    imgmedian=cv2.medianBlur(imgThres,5) #removing the pixels from imgThres where slots are empty
    kernel = np.ones((3, 3), np.uint8)#creating a matrix of size 3x3
    imgDilate= cv2.dilate(imgThres, kernel, iterations=1)  #expanding the white areas.
    check(imgDilate)
    
    cv2.imshow("Image thres", img)
    cv2.waitKey(10)