import cv2
import os

inputDir = "videos"
# capture = cv2.VideoCapture('videos/badform-back_1.avi')

for filename in os.listdir(inputDir):
    count = 0

    full_video = inputDir + "/" + filename
    capture = cv2.VideoCapture(full_video)
    while (True):
        success, frame = capture.read()

        if success and (count % 5 == 0):
            borderOutput = cv2.copyMakeBorder(frame, 0, 0, 326, 326, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            cv2.imwrite(f'frames/' + filename.split(".")[0] + "_" + str(count/5) + '.jpg', borderOutput)
        elif not success:
            # print(success)
            break
        count = count + 1
    capture.release()
