import cv2
import pickle



width, height = 107, 48 #found out the width and height by trial and error method
try:
    with open("Carpos", "rb") as file:
        pos=pickle.load(file) #if pos is already available. if not done then the image will be overwritten everytime.
except:
    pos=[]


def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN: #placing a box when you left click
        pos.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN: #deleting if you right click
        for i, p in enumerate(pos):
            x1, y1 = p
            if x1 <= x <= x1 + width and y1 <= y <= y1 + height: #checking if the click is within the boundary of the
                pos.pop(i)
                break
    with open("Carpos", "wb") as file:
        pickle.dump(pos,file) #dumping pos in file


while True:
    img=cv2.imread("parking lot image.png")
    #cv2.rectangle(img,(45,89),(162,144),(0,0,255), 2)  #used trial and error to get the correct outline
    
    for p in pos:
        cv2.rectangle(img,p,(p[0]+width,p[1]+height),(255,0,0), 2) 
    cv2.imshow("Car parking" ,img)
    cv2.setMouseCallback("Car parking", mouseclick)
    cv2.waitKey(1)