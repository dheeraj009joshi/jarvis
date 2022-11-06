import os
import cv2
import face_recognition
import pyttsx3
import speech_recognition as sr
from config import USER,BOTNAME,EMAIL,PASSWORD
from datetime import datetime

from random import choice
from utils import opening_text
from pprint import pprint
# Text to Speech Conversion
def speak(text):
    engine = pyttsx3.init('sapi5')

    # Set Rate
    engine.setProperty('rate', 190)

    # Set Volume
    engine.setProperty('volume', 4.0)

    # Set Voice (Female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()



# Greet the user
def greet_user(USERNAME):
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")




def find_encoding(images):
    encode_list=[]
    for img in images:
        # print(img)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(rgb_img)
        img_encoding = face_recognition.face_encodings(rgb_img)[0]
        encode_list.append(img_encoding)
    return encode_list



# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query