import cv2
import numpy as np 
 
cap = cv2.VideoCapture(0)  

while(1):
    green ,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    green_low_limit=np.array([24,92,112],np.uint8)
    green_high_limit=np.array([110,255,255],np.uint8)
    green_mask=cv2.inRange(hsv,green_low_limit,green_high_limit)
    kernal=np.ones((5,5),"uint8")
    green_mask=cv2.dilate(green_mask,kernal)
    res_green=cv2.bitwise_and(frame,frame,mask=green_mask)
    contours,hierarchy=cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h=cv2.boundingRect(contour)
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"Green",(x,y),cv2.FONT_ITALIC,2,(255,0,0),2)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",green_mask)
    cv2.imshow("hsv",hsv)    

    if cv2.waitKey(5) & 0xFF == ord("q"):

     cap.realise()
     cv2.destroyAllWindows()        