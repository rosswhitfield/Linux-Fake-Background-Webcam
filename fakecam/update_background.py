import cv2
import numpy

cap = cv2.VideoCapture(2)  #ignore the errors
cap.set(3, 1280)        #Set the width important because the default will timeout
                       #ignore the error or false response
cap.set(4, 720)        #Set the height ignore the errors
r, frame = cap.read()
cv2.imwrite("background.jpg", frame)
