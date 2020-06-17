# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:38:25 2020

@author: Bhanu
"""

import cv2
video=cv2.VideoCapture(r"D:\4 th semester\Projects\dsp videos\Sine.mp4")
while True:
    success,img=video.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break