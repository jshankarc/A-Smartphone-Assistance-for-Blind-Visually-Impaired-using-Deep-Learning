# A Smartphone assistance for Blind & Visually Impaired using Deep Learning: A Glimpse at Challenges

## Abstract
The study explains the primary challenges in implementing the smart assist aid to the blind and visually
impaired people to navigate easily and safely to a planned destination without depending on another person.
Besides, tremendous efforts and resources are invested against autonomous car development using AI.
However, none of these technologies are used toward people to navigate. The standard autonomous car
principle is employed to overcome the obstacle, the typical challenges found are to detect the footpath lane
pattern and train the model to detect the human turning angle in the curved street. The curvy road angle is
perceived as a regression problem and a similar turn is categorized as a direction (Left & Right) to solve as a
classification problem. Advanced algorithms are used to detect lane patterns and also illustrate the
complexities and drawbacks associated with the process.

## Literature Review Summary
Considering the decades of technological advancement, the solution to provide blind people has only been
addressed by the minority and educational segments. The numerous feasible approach presented to fix this
problem was by creating a portable device with a collection of sensors. The obvious sensor choices were
Ultrasonic sensor, Optical Sensor and Laser Sensor, these sensors worked perfectly as intended to but failed
to overall address the issue rather performed well at one specific task of the solution. The details of these
challenging factors are compared directly with the current technological advancement to comprehend the
diverged focus area and their limiting elements. The current trending approach using Microsoft Kinect depth
camera has the potential to label most of the drawbacks. Also, not only navigation being a primary focus point,
other areas such as using mobile phones and computers have advanced by enabling voice assistance, talk-back
and screen magnification features. The basic requirements for these problems are developing a highly protable,
low weight, a user-friendly and interactive device to function on all use-case scenarios just like a normal
human encounter and finds solutions using cognitive thinking. Thus, similar to all the research, this paper will
address a specific puzzle that was not viewed previous to navigate thought the curves on the road.

## Problem Statement
The problem is discussed in three different aspects in Data Analytics. To undertake blind turning angle change
in the curvy roads, a dataset of walking on road and accelerometer is applied to implement in the CNN
Regression problem. Then, classification problem direction indication as left, right and forward applied on
Forest Trails for Mobile Robots. Finally, Lane Detection pattern and their challenges in the current scenario.

## Navigation using Classification & Regression Analysis
### Classification
#### Data Source
The problem is split into two groups one uses regression technique with self-recorded footpath data along with
accelerometer to identify turning angle and another is a classifier to labeling directions namely left, right and
forward on "Visual Perception of Forest Trails for Mobile Robots" dataset.
### Regression
#### Data Source 
The core concept of this paper is inspired by an autonomous car containing a steering angle and a front-camera
record. Similarly, it is necessary to build a source that is simple yet powerful to run both machine learning and
deep learning models. To capture the data, a bike-mounted with two smartphones on the handlebar is employed
as in the above figure. The model of the two phones is Oneplus 6T and Nexus 5. Using these two smartphones,
the data is collected, Oneplus 6T is used to record the video which is kept in a vertical angle and the Nexus 5
to capture the reading of the accelerometer. The recorded data from the smartphones contains the video of the
footpath and accelerometer reading X, Y, and Z coordinates along with the time

### Exploratory Data Analysis
It is a data analysis methodology that utilizes a range of (mostly graphical) methods to optimize the visibility
into a data set, detect underlying structure, isolate relevant variables, detect outliers and exceptions, check
underlying assumptions, build parsimonious models and evaluate optimal factor settings.
Recent advances in deep learning algorithms are primarily due to the amount and variety of data collected in
recent years. Data augmentation is a technique that encourages practitioners to significantly increase the
variety of data available for training models without actually collecting new data. The basic methods such as
cropping, padding and horizontal flips with massive neural networks. Moreover, the majority of methods used
in neural networks training utilizes only basic types of augmentation. While the in-depth analysis was carried
out on neural network architectures, less emphasis was focused on finding specific forms of data augmentation
and data augmentation policies collecting data invariances. The techniques include affine transformations,
perspective transformations, contrast changes, Gaussian noise, dropout of regions, hue/saturation changes,
cropping/padding, blurring are used to produce variations in the image. The functionality to augment images
with segmentation masks, bounding boxes, key points, and heatmaps methods act as a key for transformation.
![Augumentation](https://github.com/jshankarrepo/A-Smartphone-Assistance-for-Blind-Visually-Impaired-using-Deep-Learning/blob/master/augumentation.png "augumentation.png")

## Models 
- AlexNet CNN 
- VGGNet CNN
- NVIDIA's CNN Self-Driving Car Archiecture

## Results
The experimental results have proven the findings that concluded that NVIDIA and VGGNet were the best
performing classification models with 56% and 55% accuracy respectively. AlexNet produced the least
accuracy of 46% among the three classification models. A custom CNN produced the highest accuracy of
82% among the two regression models and can be considered as our best regression model. It was closely
followed by NVIDIA with an overall accuracy of 76%. A good value for Accuracy has been achieved from
the simple CNN model.

### Lane Detection Analysis
Line detection is as important as edge detection in lane detection. This typically includes two models that
include a feather-based method and model-based methods. Some use modified Hough transform to remove
lane profile segments and use the clustering algorithm DBSCAN (Density-based spatial clustering of
applications with noise). Others use progressive probabilistic Hough transform coupled with the technology
of maximum stable extreme area (MSER) to define and detect lane lines and use the Kalman filter to achieve
continuous tracking. Nevertheless, the algorithm does not work well at night. However, in this case Hough
Transform is used to detect the lane.

#### Canny Edge Detection
![Canny Edge Detection](https://github.com/jshankarrepo/A-Smartphone-Assistance-for-Blind-Visually-Impaired-using-Deep-Learning/blob/master/canny_edge_detector.png "canny_edge_detector.png")

The picture on the left shows the black and grey image of a path and then the corresponding image next to it
after the Canny edge detector path finding algorithm has been applied to it. This technique has been applied
using three parameters which are Sigma, Low threshold and High threshold. The technique works by first
performing Gaiussian smoothing, then applying gradient and finally non-maximum suppression. The value of Sigma has been set to 10, Low threshold value is 28% and High threshold value is 42%. The resulting
image after the applying the Canny edge detector, the path of the road is accurately extracted. The second
image is of a pavement. The structure of the footpath is not entirely accurate, therefore the path detection
algorithm was not able to correctly perform as in the previous illustration.

## Conclusion
This paper presents a novel navigation challenges in implementing the smartphone assist aid for visually
impaired groups to help them reach the destination safely and efficiently in an outdoor environment. The
problem in the Data Analytics perspective is categorized into regression and classification. Regression for
determining the turning curve and classification for the direction indicator. In both cases, a very popular Deep
Learning CNN model is implemented to find the results. To predict the turning deviation a custom NVIDIA,
VGGNet, and AlexNet models are applied and in return, NVIDIA and VGGNet performed better. On the other
hand, in classification problems for guiding left, right and forward paths the standard NVIDIA performed did
not perform well compared to simple CNN models. Finally, a Lane Detection problem is elaborated to
recognize the challenges associated with it and also to resolve an issue linked to payment. Experimental results
fairly performed in some cases. The reason for these downward results is a weak dataset, lack of simulations
and footpath. Thus, visually impaired people walk from one place to another is still remains an unsolved
puzzle.






