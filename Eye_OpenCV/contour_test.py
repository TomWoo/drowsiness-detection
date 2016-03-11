import cv2
import numpy as np

# img = cv2.imread()
cv2.namedWindow('image')
border = 10

capture = cv2.VideoCapture(0)
while capture.isOpened():
    flag, img = capture.read()
    (height, width) = img.shape[:2]
    contour = np.array([(border, border), (border, height-border),
                        (width-border, height-border), (width-border, border)],
                       dtype=np.int)
    cv2.drawContours(img, [contour], -1, (255, 0, 0), 1)
    cv2.imshow('image', img)
    if cv2.waitKey(0) == ord('q'):
        exit()
