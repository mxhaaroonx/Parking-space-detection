import cv2
import pickle



width, height= 195, 70 #found out the width and height by trial and error method
pos=[]

def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        pos.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, p in enumerate(pos):
            x1, y1 = p
            if x1 <= x <= x1 + width and y1 <= y <= y1 + height:
                pos.pop(i)
                break


while True:
    #cv2.rectangle(img,(55,82),(255,166),(0,0,255), 2)  used trial and error to get the correct outline
    img=cv2.imread("Car image.png")
    for p in pos:
        cv2.rectangle(img,p,(p[0]+width,p[1]+height),(255,0,0), 2) 
    cv2.imshow("Car parking" ,img)
    cv2.setMouseCallback("Car parking", mouseclick)
    cv2.waitKey(1)