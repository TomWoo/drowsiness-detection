import cv2
from copy import copy

bg_thickness = 10
num_iterations = 300
# TODO: define path(s)
# face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_righteye.xml')
eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_big.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_small.xml')

def show_eyes(img_in):
    bw_img = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)

    # img_out,  contours,  hierarchy = cv2.findContours(bw_img,  cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)
    img_out = copy(img_in)
    # print len(contours) > 0
    # cv2.drawContours(img_out,  contours[0],  -1,  (0,  0,  255))
    return img_out

def find_eyes(img_in):
    roi_color = copy(img_in)
    roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray,  1.3,  5)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     roi_gray = gray[y:y+h,  x:x+w]
    #     roi_color = img[y:y+h,  x:x+w]
    #     eyes = eye_cascade.detectMultiScale(roi_gray)
    #     for (ex, ey, ew, eh) in eyes:
    #         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    eyes = eye_cascade.detectMultiScale(roi_gray)
    selected_eyes = None
    max_area = 0
    for (ex, ey, ew, eh) in eyes:
        area = ew*eh
        if area>max_area:
            max_area = area
            selected_eyes = (ex, ey, ew, eh)
    if selected_eyes is not None:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # TODO

    img_out = roi_color
    return img_out
