import cv2
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import mediapipe as mp
import time
import datetime
import warnings
warnings.filterwarnings("ignore")

modelpath = "KNN_model_2024-11-09_15_28_59.joblib"
print(f"Loading model {modelpath}...")
model = joblib.load(modelpath)
print("Done loading model")

print("Initializing mediapipe")
mp_pose = mp.solutions.pose
print("Finished initializing mediapipe")

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d_%H_%M_%S")
videofilename = f"workout_{formatted_date}.mp4"
frameRate = 15
out = cv2.VideoWriter(videofilename, fourcc, frameRate, (frame_width, frame_height))

headers = []
for i in range(33):
    for j in ['x','y','z','visability']:
        headers.append(f"lm_{i}_{j}")


def addText(frame, pred):
    font = cv2.FONT_HERSHEY_COMPLEX
    org = (30,50)
    fontScale = 1
    color = (255, 0,0)
    thickness = 2

    text = f"Form {pred}"
    if pred[0] == 0:
        text = "Idle"
    elif pred[0] == 1:
        text = "Bad Form"
        color = (0,0,255)
    elif pred[0] == 2:
        text = "Good Form"
        color = (0,255,0)
    else:
        text = "Unidentifiable"

    image = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

    return image


with mp_pose.Pose(
    static_image_mode=False,
    model_complexity=0,
    enable_segmentation=True,
    min_detection_confidence=0.5,
	min_tracking_confidence=0.5) as pose: 

    print("Press Q key to exit")

    while cam.isOpened():
        ret, cameraFrame = cam.read()
        if not ret:
            print("Error reading camera")
            break

        cameraFrame = cv2.flip(cameraFrame, 1)




        results = pose.process(cameraFrame)

        data = []
        if results.pose_landmarks != None:
            for landmark in results.pose_world_landmarks.landmark: 
                data.append(landmark.x)
                data.append(landmark.y)
                data.append(landmark.z)
                data.append(landmark.visibility)

            df = pandas.DataFrame(data)
            df = df.T
            df.columns = headers
            
            pred = model.predict(df)

            ts = (time.time() // 1)

            cameraFrame = addText(cameraFrame, pred)
            cv2.imwrite(f"output/{ts}.png", cameraFrame)

            #if pred > 0:
                #print(f"Prediction: {pred}")

        else:
            pass
            #("no pose detected")


        # Display the captured frame
        cv2.imshow('Camera', cameraFrame)
        out.write(cameraFrame)

            # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break


# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()
