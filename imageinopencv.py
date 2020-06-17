# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:54:55 2020

@author: Bhanu
"""
import cv2
print(cv2.__version__)
img_path=r"D:\4 th semester\Projects\DSP\misc\misc\4.1.04.tiff"
img=cv2.imread(img_path)
cv2.imshow("Output",img)
cv2.waitKey(5000)
