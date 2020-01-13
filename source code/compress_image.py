# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:06:39 2019

@author: jshan
"""
import cv2
from pathlib import Path
from PIL import Image
import numpy
 
scale_percent = 90 # percent of original size
        
def comporess_and_write(file, split_dir, direction, index):
    pil_image = Image.open(file)
    img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    path = "compressed_data/" + split_dir + "/" + direction + "/frame_" + str(index) + ".jpg"
    print("path::", path)
    cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY), 60] )
        
        
r_count = 1
l_count = 1
c_count = 1
total_left_count = 0
total_right_count = 0
total_center_count = 0

left_train_count = 0
right_train_count = 0
center_train_count = 0

left_test_count = 0
right_test_count = 0
center_test_count = 0

left_valid_count = 0
right_valid_count = 0
center_valid_count = 0

image_dir = Path("C:\\Users\\jshan\\Desktop\\navigation_dataset_test\\")

folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
for i, direc in enumerate(folders):
    for file in direc.iterdir():
        if "lc" in str(file):
            total_left_count += 1
        if "rc" in str(file):
            total_right_count += 1
        if "sc" in str(file):
            total_center_count += 1    
    
left_train_count = numpy.round(total_left_count / 100 * 60)
right_train_count = numpy.round(total_right_count / 100 * 60 )
center_train_count = numpy.round(total_center_count / 100 * 60 )

left_test_count = numpy.round(total_left_count / 100 * 30 + left_train_count)
right_test_count = numpy.round(total_right_count / 100 * 30 + right_train_count)
center_test_count = numpy.round(total_center_count / 100 * 30 + center_train_count)

left_valid_count = numpy.round(total_left_count / 100 * 10 + left_test_count)
right_valid_count = numpy.round(total_right_count / 100 * 10 + right_test_count)
center_valid_count = numpy.round(total_center_count / 100 * 10 + center_test_count)
print("Total Count::Left:{}::Right:{}::Center:{}".format(total_left_count, total_right_count, total_center_count))
print("Split Count::Left::train:{}::test:{}::valid:{}::Right::train:{}::test:{}::valid:{}::Center::train:{}::test:{}::valid:{}".format( 
      left_train_count, left_test_count, left_valid_count, right_train_count,right_test_count,right_valid_count,center_train_count, center_test_count,center_valid_count))
for i, direc in enumerate(folders):
    for file in direc.iterdir():
        
        if "lc" in str(file) and l_count < left_train_count:
            comporess_and_write(file, 'train', 'left', l_count )
            l_count += 1
        
        elif "lc" in str(file) and l_count < left_test_count:
            comporess_and_write(file, 'test', 'left', l_count)
            l_count += 1
            
        elif "lc" in str(file) and l_count < left_valid_count:
            comporess_and_write(file, 'valid', 'left', l_count)
            l_count += 1

            
        if "rc" in str(file) and r_count < right_train_count:
            comporess_and_write(file, 'train', 'right', l_count)
            r_count += 1

        elif "rc" in str(file) and r_count < right_test_count:
            comporess_and_write(file, 'test', 'right', l_count)
            r_count += 1

        elif "rc" in str(file) and r_count < right_valid_count:
            comporess_and_write(file, 'valid', 'right', l_count)
            r_count += 1

            
        if "sc" in str(file) and c_count < center_train_count:
            comporess_and_write(file, 'train', 'center', l_count)
            c_count += 1
            
        elif "sc" in str(file) and c_count < center_test_count:
            comporess_and_write(file, 'test', 'center', l_count)
            c_count += 1
            
        elif "sc" in str(file) and c_count < center_valid_count:
            comporess_and_write(file, 'valid', 'center', l_count)
            c_count += 1
        

