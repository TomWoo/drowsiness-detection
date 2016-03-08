import cv2
import eyes

# path = 'C:/Users/User/OneDrive/Duke/6_Spring_2016/ECE_590/drowsiness-detection/Training_Data/images/Tom/'
# files = ['right_1.png', 'right_2.png']
# length = len(files)
# filenames = [0] * length
# for i in range(length):
#     filenames[i] = path + files[i]
capture = cv2.VideoCapture(0)
length = 10000

cv2.namedWindow('in')
cv2.namedWindow('out')
i = 0
key = -1
for i in range(length):
    success, img = capture.read()
    # img = cv2.imread(filenames[i], cv2.IMREAD_COLOR)
    if img is not None:
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
    else:
        print 'no input'
        break
    i += 1
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
