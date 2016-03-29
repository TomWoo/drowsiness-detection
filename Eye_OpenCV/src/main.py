import cv2
import time
import eyes
import contour
import matplotlib.pyplot as plt
import os

filepath = os.path.dirname(os.path.dirname(os.path.abspath( __file__ )))  # Eye_OpenCV folder path
INPUT_FILE_PATH = os.path.join(filepath, 'inputFiles\\inputTom.mp4')
OUTPUT_FILE_PATH = os.path.join(filepath, 'outputFiles\\detectedEyes.avi')
# path = 'C:/Users/User/OneDrive/Duke/6_Spring_2016/ECE_590/drowsiness-detection/Training_Data/images/Tom/'
# files = ['right_1.png', 'right_2.png']
# length = len(files)
# filenames = [0] * length
# for i in range(length):
#     filenames[i] = path + files[i]

# capture = cv2.VideoCapture(0)  # TODO: use next line instead for video instead of webcam
capture = cv2.VideoCapture(INPUT_FILE_PATH)
scale = 0.80  # TODO: decrease slightly for performance, but not too much; otherwise can be buggy
border = 10  # TODO: optimize negative mask region (currently a border around positive mask region/rectangle); more or less optimized for myself

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # TODO: platform dependent video output; check using python os
# TODO: establish relative path
out = cv2.VideoWriter(OUTPUT_FILE_PATH, fourcc, 20.0, (640, 480))

# Timeseries
t_series = []
percentage_open_series = []
blink_series = []
plt.ion()
plt.show()
init_time = time.time()

# cv2.namedWindow('in')
cv2.namedWindow('out')
# i = 0
key = -1
while capture.grab():  # capture.isOpened():
    start_time = time.time()

    success, img = capture.read()
    # img = cv2.imread(filenames[i], cv2.IMREAD_COLOR)
    if img is not None:
        (height, width) = img.shape[:2]
        img = cv2.resize(img, (int(width*scale), int(height*scale)), interpolation=cv2.INTER_AREA)
        (height, width) = img.shape[:2]
        if height > 0 and width > 0:
            # cv2.imshow('in', img)
            # cv2.moveWindow('in', 400, 0)
            # cv2.resizeWindow('in', 400, 400)
            # img_out = eyes.show_eyes(img)
            eye_rect = eyes.find_eyes(img, border)
            # cv2.imshow('out', img)
            # eye_rect = contour.find_bounding_rect(img)
            img_out = contour.draw_rect_contour(img, eye_rect)
            cv2.imshow('out', img_out)

            # # Plot timeseries
            total_elapsed_time = time.time() - init_time
            percentage_eye_open = 0.0
            if (eye_rect[2] > 0) and (eye_rect[3] > 0):
                percentage_eye_open = 1.0*eye_rect[3]/eye_rect[2]
            print 'width = ' + str(eye_rect[2])
            print 'height = ' + str(eye_rect[3])
            print 'percentage_eye_open = ' + str(percentage_eye_open)
            t_series.append(total_elapsed_time)
            percentage_open_series.append(percentage_eye_open)

            # TODO: comment out graphing for performance
            # plt.axis([0, total_elapsed_time+1, 0, 1])
            # # plt.plot(t_series, percentage_open_series)
            # plt.scatter(t_series, percentage_open_series)
            # plt.draw()
            # plt.pause(0.001)
        else:
            print 'zero size'
            break

        elapsed_time = time.time() - start_time
        fps = 1/elapsed_time
        # print 'fps = ' + str(fps)
        # TODO: comment out video output for performance
        # num_frames_out = int(30/fps)
        # for i in range(num_frames_out):
        #     out.write(img_out)
    else:
        print 'no input'
        break
    # i += 1
    if cv2.waitKey(30) == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
