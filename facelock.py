import cv2
import face_recognition
import os
import time
import numpy as np
from functions import find_encoding, speak
# from jarvis import jarvis


def faceLocksyatem():
    cap = cv2.VideoCapture(0)
    # scaling_factor=0.5
    path="images"
    images=[]
    className=[]
    myList=os.listdir(path)

    for cl in myList:
        curImg= cv2.imread((f'{path}/{cl}'))
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])
    print(className)
    NAME=""
    while NAME=="":
        # print()
        ret, frame = cap.read()
        imgs=cv2.resize(frame,(0,0),None,0.25,0.25)
        imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
        faces_current=face_recognition.face_locations(imgs)
        encoding_current = face_recognition.face_encodings(imgs,faces_current)
        print("done")
        
        for encodeFace,faceLoc in zip(encoding_current,faces_current):
            print("Comparing Face")
            matches=face_recognition.compare_faces(find_encoding(images),encodeFace)
            faceDis=face_recognition.face_distance(find_encoding(images),encodeFace)
            match_index=np.argmin(faceDis)
            if matches[match_index]:
                NAME=className[match_index]
                print(NAME)
                break
            else:
                speak("User Not Found !")
                print("Retrying.......")
        
    return NAME
                
        
# ad=faceLocksyatem()
# print(ad)