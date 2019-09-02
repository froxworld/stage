import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--name", help="video nam")
args = parser.parse_args()



# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(args.name)

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Erreur en ouvrant le fichier {0}".format(args.name))

# Read until video is completed
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame',cv2.resize(frame, (640,480)))
        # Press Q on keyboard to  exit
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
