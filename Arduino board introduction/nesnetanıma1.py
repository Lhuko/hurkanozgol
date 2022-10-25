from ast import Break, While
import cv2
import numpy as np 

arduino=cv2.CascadeClassifier("arduino.xml")
webcam=cv2.VideoCapture(0)
while True:
    kontrol,cerceve=webcam.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    sonuc=arduino.detectMultiScale(gri,1.1,4)
    for (x,y,genislik,yukseklik) in sonuc:
        cv2.putText(cerceve,"Arduino",(x,y),cv2.FONT_ITALIC,2,(255,0,0),2)
        cv2.rectangle(cerceve,(x,y),(x+genislik,y+yukseklik),(255,0,0),2)
    if cv2.waitKey(5)==27:
        break
    cv2.imshow("Tespit",cerceve)

    





         
    

