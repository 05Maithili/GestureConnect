from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import pyttsx3
import cv2
import time
import mediapipe as mp
from googletrans import Translator
import threading
from gtts import gTTS
import os

def home(request):
    return render(request,'home.html')

def sign_to_text(request):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)  # Open the webcam

    start_time = time.time()
    detected_gesture = "No gesture detected"

    while True:
        success, img = cap.read()
        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            detected_gesture = "Gesture Detected"  # Placeholder: You can map gestures to words here
            break  # Stop after detecting a gesture

        cv2.imshow("Gesture Recognition", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'sign_to_text.html', {"recognized_text": detected_gesture})

def sign_to_speech(request):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils
    engine = pyttsx3.init()

    cap = cv2.VideoCapture(0)  # Open the webcam

    start_time = time.time()
    detected_gesture = "No gesture detected"

    while True:
        success, img = cap.read()
        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            detected_gesture = "Gesture Detected"  # Placeholder: Replace with actual gesture detection logic
            engine.say(detected_gesture)  # Convert detected gesture into speech
            engine.runAndWait()
            break  # Stop after detecting a gesture

        cv2.imshow("Sign to Speech", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'sign_to_speech.html', {"spoken_text": detected_gesture})

def text_to_speech(request):
    text = "Hello, welcome to GestureConnect!"  # Default text
    audio_file = "static/speech.mp3"  # Path to save the audio file

    # Convert text to speech
    tts = gTTS(text=text, lang="en")
    tts.save(audio_file)

    return render(request, 'text_to_speech.html', {"audio_url": audio_file})

def speech_to_text(request):
    recognizer = sr.Recognizer()
    detected_text = "No speech detected"

    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source)  # No timeout
  # Listen for speech
            detected_text = recognizer.recognize_google(audio)  # Convert speech to text using Google API
        except sr.UnknownValueError:
            detected_text = "Sorry, could not understand the audio."
        except sr.RequestError:
            detected_text = "Error with the speech recognition service."

    return render(request, 'speech_to_text.html', {"converted_text": detected_text})

def signup_signin(request):
    return render(request,'signup_signin.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

def contact(request):
    return render(request,'contact.html')
