# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:11:04 2017

@author: Sampath
"""

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

#pts_rshp = np.reshape(pts,(-1,1,2),order='C')
img_poly = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('test',img_poly)
cv2.waitKey(0)
cv2.destroyAllWindows()