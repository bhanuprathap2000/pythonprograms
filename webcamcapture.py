# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:57:51 2020

@author: Bhanu
"""

import cv2
video=cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
while True:
    success,img=video.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break