# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:05:01 2021

@author: Mehmet Akıncı
"""
from detect import Detect
import cv2
img = cv2.imread("Photos/img_6.jpg")

cv2.imshow("Output",Detect(img))
cv2.waitKey(0)


"""cap = cv2.VideoCapture("Photos/video_2.mp4")

while True:
    success,img = cap.read()
    #img = cv2.resize(img, (640,640))
    #cv2.imshow("Original",img)
    cv2.imshow("Video",Detect(img))
    if cv2.waitKey(1) == 27: 
            break  # esc to quit

cap.release()"""
cv2.destroyAllWindows()