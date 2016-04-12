import cv2
import time
import eyes
import contour
import matplotlib.pyplot as plt
import os

# Eye_OpenCV folder path
filepath = os.path.dirname(os.path.dirname(os.path.abspath( __file__ ))) 
#posix for UNIX systems and nt for WIN
if 'posix' in os.name:
    INPUT_FILE_PATH = os.path.join(filepath, 'inputFiles/inputTom.mp4')
    OUTPUT_FILE_PATH = os.path.join(filepath, 'outputFiles/detectedEyes.avi')
elif 'nt' in os.name:
    INPUT_FILE_PATH = os.path.join(filepath, 'inputFiles\\inputTom.mp4')
    OUTPUT_FILE_PATH = os.path.join(filepath, 'outputFiles\\detectedEyes.avi')
else:
    print "Horridly Unsupported OS! Bamn!"
    exit()
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

if 'posix' in os.name:
    fourcc = cv2.cv.CV_FOURCC(*'MJPG')
elif 'nt' in os.name:
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
else: 
    print "Horridly Unsupported OS! Bamn!"
    exit()
# TODO: establish relative path
out = cv2.VideoWriter(OUTPUT_FILE_PATH, fourcc, 20.0, (640, 480))

# Timeseries
t_series =  []
percentage_open_series = []
min_val_series = []
blink_series = []
plt.ion()
plt.show()
init_time = time.time()

# cv2.namedWindow('in')
cv2.namedWindow('out')
# i = 0
key = -1
count = 0
min_val = 1
max_val = 1
percentageClosureList = list()
percentageClosureList.append(100)
eyeStatusList = list()
eyeOpen = True
closedCounter = 0
blinkCounter = 0
openCounter = 0
openStartFrame = 0
closedStartFrame = 0
frameNumber = 0
openDuration = dict()
openDuration["duration"] = list()
openDuration["startFrame"] = list()
closedDuration = dict()
closedDuration["duration"] = list()
closedDuration["startFrame"] = list()

def isClosing():
    return percentageClosureList[-1] < 60 and percentageClosureList[-2] > 60

def isOpening():
    return percentageClosureList[-1] > 60 and percentageClosureList[-2] < 60


print "Starting to process frames"
while capture.isOpened():     
    start_time = time.time()    
    time.sleep(0.5)
    # Capture video frame-by-frame
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
            if count == 0:
                template = eye_rect
                count = count + 1 
            else:
                res = cv2.matchTemplate(eye_rect,template,eval('cv2.TM_CCORR_NORMED'))
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                #print "Min Value ", min_val, "Max Value", max_val

            if min_val >= 0.985:
                nextGraphVal = 100
            elif min_val < 0.985 and min_val >= 0.96:
                nextGraphVal = 80
            elif min_val < 0.96 and min_val >= 0.945:
                nextGraphVal = 50
            elif min_val < 0.945 and min_val >= 0.92:
                nextGraphVal = 20
            elif min_val <0.92:
                nextGraphVal = 0
            cv2.imshow('out', eye_rect)
            
            percentageClosureList.append(nextGraphVal)

            # Calculating duration of eye closure
            if isClosing() :
                closedCounter = 0
                closedStartFrame = frameNumber
                print("\t\t\t\t\t BLINK STARTED")
                print "\t\t\t\t\t OPEN DURATION (FRAMES) " , openCounter
                openDuration["duration"].append(openCounter)
                openDuration["startFrame"].append(openStartFrame)
            if isOpening() :
                print("\t\t\t\t\t BLINK ENDED")
                print "\t\t\t\t\t CLOSED DURATION (FRAMES) " , closedCounter
                blinkCounter = blinkCounter + 1
                openCounter = 0
                openStartFrame = frameNumber
                closedDuration["duration"].append(closedCounter)
                closedDuration["startFrame"].append(closedStartFrame)

            print nextGraphVal, "% open"
            print "openList", openDuration
            print "closedList", closedDuration

            if(percentageClosureList[-1]<60):
                eyeOpen = False
            else:
                eyeOpen = True

            if eyeOpen:
                openCounter = openCounter + 1
            else:
                closedCounter = closedCounter + 1

            # Plotting graph of percentage closures
            #plt.plot(percentageClosureList, '.-')
            #plt.ylim([-10, 110])

            # eye_rect = contour.find_bounding_rect(img)
            #img_out = contour.draw_rect_contour(img, eye_rect)
            #cv2.imshow('out', img_out)

            # # Plot timeseries
            # total_elapsed_time = time.time() - init_time
            # percentage_eye_open = 0.0
            # if (eye_rect[2] > 0) and (eye_rect[3] > 0):
            #     percentage_eye_open = 1.0*eye_rect[3]/eye_rect[2]
            # print 'width = ' + str(eye_rect[2])
            # print 'height = ' + str(eye_rect[3])
            #print 'percentage_eye_open = ' + str(percentage_eye_open)
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
    frameNumber = frameNumber + 1

capture.release()
out.release()
cv2.destroyAllWindows()