import cv2
from copy import copy

bg_thickness = 10
num_iterations = 300
# TODO: place files in the same dir
face_cascade = cv2.CascadeClassifier('C:\Users\User\Desktop\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Users\User\Desktop\opencv\sources\data\haarcascades\haarcascade_eye.xml')

def show_eyes(img_in):
    bw_img = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)

    # img_out, contours, hierarchy = cv2.findContours(bw_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_out = copy(img_in)
    # print len(contours) > 0
    # cv2.drawContours(img_out, contours[0], -1, (0, 0, 255))
    return img_out

def find_eyes(img_in):
    img = copy(img_in)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img
