import cv2
# import cv
import eyes
import time

# path = 'C:/Users/User/OneDrive/Duke/6_Spring_2016/ECE_590/drowsiness-detection/Training_Data/images/Tom/'
# files = ['right_1.png', 'right_2.png']
# length = len(files)
# filenames = [0] * length
# for i in range(length):
#     filenames[i] = path + files[i]
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('C:/Users/User/OneDrive/Duke/6_Spring_2016/ECE_590/drowsiness-detection/Training_Data/Videos/Tom/20160220_110118.mp4')
scale = 0.25

# cv2.namedWindow('in')
cv2.namedWindow('out')
i = 0
key = -1
while capture.isOpened():
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
            img_out = eyes.find_eyes(img)
            cv2.imshow('out', img_out)
        else:
            print 'zero size'
            break

        elapsed_time = time.time() - start_time
        fps = 1/elapsed_time
        print 'fps = ' + str(fps)
    else:
        print 'no input'
        break
    i += 1
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
