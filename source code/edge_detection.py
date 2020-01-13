# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:12:17 2019

@author: jshan
"""

from utils import utils
import numpy as np
import cv2
import canny_edge_detector as ced

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image


imgs = utils.load_data()
utils.visualize(imgs, 'gray')


detector = ced.cannyEdgeDetector(imgs, sigma=9, kernel_size=9, lowthreshold=0.5, highthreshold=0.48, weak_pixel=1000)

imgs_final = detector.detect()
utils.visualize(imgs_final, 'gray')

lines = cv2.HoughLinesP(imgs_final, 1, np.pi/180, 1, np.array([]), minLineLength = 100, maxLineGap = 20)
line_image = display_lines(imgs_final, lines)
utils.visualize(line_image, 'gray')