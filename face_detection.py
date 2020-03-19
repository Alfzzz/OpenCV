import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(2) #Change to 0 for computer camera and 1 for default camera  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame',frame)	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

