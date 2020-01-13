# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:51:27 2019

@author: jshan
"""
import cv2
from scipy import ndimage
vidcap = cv2.VideoCapture('dataset/VID_20191119_153333.mp4')
scale_percent = 60 # percent of original size

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    
    if hasFrames:
        image = ndimage.rotate(image, 270)
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite("dataset/images/image_%d.jpg" % count,image,[int(cv2.IMWRITE_JPEG_QUALITY), 20] )
        
    return hasFrames

count = 1
sec = 0
success = getFrame(sec) 
frameRate = 0.1 
while success:
    count += 1
    print("Count Value", count)
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    
