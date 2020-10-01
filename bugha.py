import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def gaali(name):
    speak("Oh i know him ,"+name+" is asshole")

def shutdown():
    speak("Shutdowning your computer... Please close all the applications running")
    time.sleep(10)
    os.system("shutdown /s /t 1")
    
def music():
    music_dir="E:\Songs"
    songs=os.listdir(music_dir)
    print(songs)
    if len(songs)==0:
        speak("You dont have any music")
    else:
        os.startfile(os.path.join(music_dir,songs[0]))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning,Rahul")
    elif hour>12 and hour<18:
        speak("Good afternoon,Rahul")
    else:
        speak("Good evening,Rahul")
    speak("Can i do something for you right now")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold=500
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print("User said:",query)
    except Exception as e:
        print(e)
        print("Please say that again..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=2)
                print(results)
                speak("Acording to Wikipedia"+results)
            except Exception as e:
                speak("You are getting"+e)
        elif "open google" in query:
            webbrowser.open("goole.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H,%M,%S")
            speak(strTime)
        elif "don't listen" or "please leave" in query:
            break
        elif "play music" in query:
            music()
        elif "shutdown my computer" in query:
            shutdown()
        elif "rajeev" or "rajiv" in query:
            gaali("rajeev")


