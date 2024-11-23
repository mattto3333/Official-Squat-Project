import os
import glob
import cv2
import mediapipe as mp
import time
import numpy as np

mp_pose = mp.solutions.pose

badformpath = "dataset\\badform"
goodformpath = "dataset\\goodform"
idleformpath = "dataset\\idleform"

badformimagepath = []
goodformimagepath = []
idleformimagepath = []

for file in glob.glob(badformpath+"/*.jpg"):
    badformimagepath.append(file)

for file in glob.glob(goodformpath+"/*.jpg"):
    goodformimagepath.append(file)


for file in glob.glob(idleformpath+"/*.jpg"):
    idleformimagepath.append(file)

print(badformimagepath)
image = cv2.imread(badformimagepath[0])


def processbatch(images_paths, label, pose, text_file):
    # 0 idle; 1 = bad, 2 = goodform
    for imagepath in images_paths:
        print(f'processing {imagepath}')
        image = cv2.imread(imagepath)

        results = pose.process(image)

        output_string = f'{imagepath},{label}'
        if results.pose_landmarks != None:
    #        print(results.pose_world_landmarks[0])
            #help(results.pose_world_landmarks)
            for landmark in results.pose_world_landmarks.landmark: 
                output_string = f'{output_string},{landmark.x},{landmark.y},{landmark.z},{landmark.visibility}'

            output_string = f'{output_string}\n'
            text_file.write(output_string)
        else:
            pass
            #print('No Pose Detected')    


def writeHeaders(text_file):
    header = 'image_path,label'
    for i in range(33):
        for j in ['x','y','z','visability']:
            header = f"{header},lm_{i}_{j}"

    text_file.write(header)
    text_file.write('\n')
    

with mp_pose.Pose(
	min_detection_confidence=0.5,
	min_tracking_confidence=0.5) as pose:

    text_file = open("Output.csv", "w")

    # 0 idle; 1 = bad, 2 = goodform
    writeHeaders(text_file)
    processbatch(badformimagepath, 1, pose, text_file)
    processbatch(goodformimagepath, 2, pose, text_file)
    processbatch(idleformimagepath, 0, pose, text_file)
    '''
    for imagepath in badformimagepath:
        image = cv2.imread(imagepath)

        results = pose.process(image)

        # 0 idle; 1 = bad, 2 = goodform
        output_string = f'{imagepath},0'
        if results.pose_landmarks != None:
    #        print(results.pose_world_landmarks[0])
            #help(results.pose_world_landmarks)
            for landmark in results.pose_world_landmarks.landmark: 
                output_string = f'{output_string},{landmark.x},{landmark.y},{landmark.z},{landmark.visibility}'

            output_string = f'{output_string}\n'
            text_file.write(output_string)
        else:
            print('No Pose Detected')
    '''
    text_file.close()

				

#cv2.imshow("image", image)
#cv2.waitKey(0)