import cv2
import numpy as np
from copy import copy

def draw_rect_contour(img_in, rect):
    img = copy(img_in)
    (x, y, width, height) = rect
    contour = np.array([(x, y), (x, y+height),
                        (x+width, y+height), (x+width, y)],
                       dtype=np.int)
    cv2.drawContours(img, [contour], -1, (0, 0, 255), 1)
    return img

def find_bounding_rect(img_in):
    mask = cv2.inRange(img_in, (1,1,1), (255,255,255))
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    contour = None
    max_area = 0.0
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > max_area:
            contour = contours[i]
            max_area = cv2.contourArea(contours[i])

    return cv2.boundingRect(contour)
