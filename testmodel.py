import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import cv2
import mediapipe as mp

model = joblib.load("KNN_model.joblib")
testimagepath = "dataset\\goodform\\5.jpg"
mp_pose = mp.solutions.pose

with mp_pose.Pose(
	min_detection_confidence=0.5,
	min_tracking_confidence=0.5) as pose:

    image = cv2.imread(testimagepath)

    results = pose.process(image)

    data = []
    if results.pose_landmarks != None:
        for landmark in results.pose_world_landmarks.landmark: 
            data.append(landmark.x)
            data.append(landmark.y)
            data.append(landmark.z)
            data.append(landmark.visibility)

            header = 'image_path,label' 

        headers = []
        for i in range(33):
            for j in ['x','y','z','visability']:
                headers.append(f"lm_{i}_{j}")



        df = pandas.DataFrame(data)
        df = df.T
        df.columns = headers
        pred = model.predict(df)

        print(f"Prediction: {pred}")


    else:
        print("no pose detected")