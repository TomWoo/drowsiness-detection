import cv2
# import cv
import numpy as np
from copy import copy

# TODO: define path(s)
# face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_righteye.xml')
eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_big.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_small.xml')

# Mask parameters
border = 5
width_reduction_factor = 1.1

# Grabcut parameters
num_iters = 1

# Snake parameters
# num_iters = 300
# alpha = 0.1  # Weight of continuity energy
# beta = 0.4  # Weight of curvature energy
# gamma = 0.5  # Weight of image energy

def show_eyes(img_in):
    bw_img = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)

    # img_out,  contours,  hierarchy = cv2.findContours(bw_img,  cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)
    img_out = copy(img_in)
    # print len(contours) > 0
    # cv2.drawContours(img_out, contours[0], -1,  (0, 0, 255))
    return img_out

def find_eyes(img_in, eng):
    img = copy(img_in)

    # ROI
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(img_gray)
    eyes_rect = None
    max_area = 0
    for (x, y, width, height) in eyes:
        area = width*height
        if area > max_area:
            max_area = area
            eyes_rect = (x, y, width, height)
    # if eyes_rect is not None:
    #     cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
    (x, y, width, height) = eyes_rect

    # Grabcut
    eyes_roi = img[y:y+height,x:x+width]
    mask = np.zeros(eyes_roi.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    right_eye_rect = (border, border, int(width/width_reduction_factor), height-border)
    cv2.grabCut(eyes_roi,mask,right_eye_rect,bgdModel,fgdModel,num_iters,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    eyes_roi = eyes_roi*mask2[:,:,np.newaxis]

    img_out = cv2.resize(eyes_roi, (2*width, 2*height))
    return img_out
