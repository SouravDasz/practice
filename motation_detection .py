import cv2 
import numpy as np 

video=cv2.VideoCapture(0)
frames=[]
gap=5
counter=0
while True:
    ret,frame=video.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frames.append(gray)

    if len(frames)>gap+1:
        frames.pop(0)
    cv2.putText(frame,f"fram no is {counter}",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    counter+=1
    if len(frames)> gap:
        diff=cv2.absdiff(frames[0],frames[-1])
        _,thresh=cv2.threshold(diff,30,255,cv2.THRESH_BINARY)
        contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour)<500:
                continue
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
            motaion =cv2.contourArea(contour)
            if motaion>500:
                cv2.putText(frame,"Motion Detected",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Motion Detection",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
