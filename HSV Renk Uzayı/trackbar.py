import cv2
import numpy as np 

cap = cv2.VideoCapture(0)


def bosluk(a):

    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,360)
cv2.createTrackbar("Hue Min","Trackbars",0,359,bosluk)
cv2.createTrackbar("Hue Max","Trackbars",0,359,bosluk)
cv2.createTrackbar("Satur Min","Trackbars",0,255,bosluk)
cv2.createTrackbar("Satur Max","Trackbars",0,255,bosluk)
cv2.createTrackbar("Value Min","Trackbars",0,255,bosluk)
cv2.createTrackbar("Value Max","Trackbars",0,255,bosluk)


while(1):
    _ ,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_min=int(cv2.getTrackbarPos("Hue Min","Trackbars") / 2)
    h_max=int(cv2.getTrackbarPos("Hue Max","Trackbars") / 2)
    s_min=cv2.getTrackbarPos("Satur Min","Trackbars")
    s_max=cv2.getTrackbarPos("Satur Min","Trackbars")
    v_min=cv2.getTrackbarPos("Value Min","Trackbars")
    v_max=cv2.getTrackbarPos("Value Max","Trackbars")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(hsv,lower,upper)

    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    # cv2.imshow("hsv",hsv)  Ekran karmaşasından dolayı görmek istemiyorum.
    cv2.imshow("Masked",mask)
    cv2.imshow("res",res)
    
    if cv2.waitKey(5) & 0xFF == ord("q"):

     cap.realise()
     cv2.destroyAllWindows()      
 




