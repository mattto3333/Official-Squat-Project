1. Navigate to the Picture Grabber folder and put the video you want to grab frames from into the video folder in there
- Run the framespliiter.py code to get the frames into the frames folder
- Move the old video into the processed videos folder

2. Navigate back to the main folder and put the images into the respective folders in the dataset folder
- dataset/goodform
- dataset/badform
- dataset/idleform

3. Run the extractdata.py code
- It will run through all the images in the above folders and get all the points from the pose estimation with mediapipe
- It saves the output into the Output.csv file in the following format: 
image_path,label,lm_0_x,lm_0_y,lm_0_z,lm_0_visability,...,lm_32_x,lm_32_y,lm_32_z,lm_32_visability

4. Run the traindata.py code
- It will open the Output.csv file and train a prediction model using KNN classifier
- The output will be in a KNN_model_[timestamp].joblib

5. Run the videocapturetest.py code
- Remeber to update the file with the newest traindata.py output prediction model (line 13)
- It will do live predictions using the webcam
- Hit "Q" to exit
