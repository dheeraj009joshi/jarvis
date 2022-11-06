from deepface import DeepFace
import cv2

from functions import speak
cap = cv2.VideoCapture(0)


# while 1:
#         # print()
#         ret, frame = cap.read()
#         print(frame)
#         



import cv2
import time
#Initialize video capture
cap = cv2.VideoCapture(0)
#scaling factor
scaling_factor = 0.5
# Loop until you hit the Esc key
while True:
    ret, frame = cap.read()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    face_analysis = DeepFace.analyze(img_path = "saved_img.jpg")
    print(face_analysis)
    print(face_analysis['dominant_race'])
    print(face_analysis['dominant_emotion'])
    speak(f"Hey you are {face_analysis['dominant_emotion'] } !")
    time.sleep(2)

    
   
