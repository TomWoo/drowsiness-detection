import cv2
# import cv
import numpy as np
from copy import copy
import contour

# TODO: define path(s)
# face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_righteye.xml')
eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_big.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_small.xml')

# Mask parameters
width_reduction_factor = 0.5

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

def find_eyes(img_in, border):
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

    if (eyes_rect is None) or (eyes_rect[2]*eyes_rect[3] <= border*border):
        return (0, 0, 0, 0)
    (global_x, global_y, global_w, global_h) = eyes_rect
    x = eyes_rect[0]-border
    y = eyes_rect[1]-border
    width = eyes_rect[2]+2*border
    height = eyes_rect[3]+2*border

    # Grabcut
    eyes_roi = img[y:y+height,x:x+width]
    mask = np.zeros(eyes_roi.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    reduced_width = int(width*width_reduction_factor)
    right_eye_rect = (border, border, width-2*border, height-2*border)
    cv2.grabCut(eyes_roi,mask,right_eye_rect,bgdModel,fgdModel,num_iters,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    eyes_roi = eyes_roi*mask2[:,:,np.newaxis]
    eyes_roi[:height, width-reduced_width:, :] = np.zeros((height, reduced_width, 3), np.uint8)

    # img_out = cv2.resize(eyes_roi, (2*width, 2*height))
    # img_out = contour.draw_rect_contour(eyes_roi, right_eye_rect)
    local_eye_rect = contour.find_bounding_rect(eyes_roi)
    # TODO: fix position offset hack!
    return (local_eye_rect[0]+global_x, local_eye_rect[1]+global_y-global_h/4, local_eye_rect[2], local_eye_rect[3])
