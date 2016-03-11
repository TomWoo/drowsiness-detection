import cv2
# import cv
import numpy as np
from copy import copy
# import matlab

# import sys
# sys.path.append('C:/Users/User/OneDrive/Duke/6_Spring_2016/ECE_590/drowsiness-detection/Eye_OpenCV/morphsnakes')
# import morphsnakes
# import test_snakes
# from matplotlib import pyplot as ppl
# ppl.figure()

# TODO: define path(s)
# face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_righteye.xml')
eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_big.xml')
# eye_cascade = cv2.CascadeClassifier('C:/Program Files/MATLAB/R2015b/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_mcs_eyepair_small.xml')

# Snake param's
border = 10
# num_iterations = 300
alpha = 0.1  # Weight of continuity energy
beta = 0.4  # Weight of curvature energy
gamma = 0.5  # Weight of image energy

def show_eyes(img_in):
    bw_img = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)

    # img_out,  contours,  hierarchy = cv2.findContours(bw_img,  cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)
    img_out = copy(img_in)
    # print len(contours) > 0
    # cv2.drawContours(img_out, contours[0], -1,  (0, 0, 255))
    return img_out

def find_eyes(img_in, eng):
    roi_color = copy(img_in)
    roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = img[y:y+h, x:x+w]
    #     eyes = eye_cascade.detectMultiScale(roi_gray)
    #     for (ex, ey, ew, eh) in eyes:
    #         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    eyes = eye_cascade.detectMultiScale(roi_gray)
    selected_eyes = None
    max_area = 0
    for (ex, ey, ew, eh) in eyes:
        area = ew*eh
        if area > max_area:
            max_area = area
            selected_eyes = (ex, ey, ew, eh)
    if selected_eyes is not None:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    eye_region_colored = roi_color[ey:ey+eh, ex:ex+ew]
    eye_region = roi_gray[ey:ey+eh, ex:ex+ew]
    (height, width) = eye_region.shape[:2]

    # # TODO
    # gI = morphsnakes.gborders(eye_region, alpha=1000, sigma=5.48)
    #
    # # Morphological GAC. Initialization of the level-set.
    # mgac = morphsnakes.MorphGAC(gI, smoothing=1, threshold=0.31, balloon=1)
    # mgac.levelset = test_snakes.circle_levelset(eye_region.shape, (height/2, width/4), 20)
    #
    # # Visual evolution.
    # morphsnakes.evolve_visual(mgac, num_iters=45, background=eye_region_colored)
    # ppl.clf()

    # (height, width) = roi_gray.shape[:2]
    # bitmap = cv.CreateImageHeader((height, width), cv.IPL_DEPTH_8U, 1)
    # cv.SetData(bitmap, roi_gray.tostring(),
    #            roi_gray.dtype.itemsize * 3 * width)
    # contour = np.array([(border, border), (border, height-border),
    #                     (width-border, height-border), (width-border, border)],
    #                    dtype=np.int)
    # contour = [(border, border), (height-border, width-border)]
    # contour = cv.SnakeImage(bitmap, contour, alpha, beta, gamma, (3, 3), (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 10, 0.01))
    # img_out = np.asarray(bitmap[:, :])

    # roi_size = eye_region.shape[:2]
    # m_img_in = matlab.uint8(eye_region)
    # m_img_out = eng.get_eye(m_img_in)
    # img_out = m_img_out.reshape(roi_size)

    img_out = roi_color
    return img_out
