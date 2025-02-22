import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0<=hour>12:
        speak("Good Morning")
    elif 12<=hour>18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi I am Jarvis, how may I help you?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold= 1  # Put equate not in bracket 
        audio = r.listen(source)
    try:
        print("Recognizing")
        query= r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again Please")
        return "None"
    return query

if __name__ == "__main__": # Put main in double hyphen
    wishMe()
    

    if 1:
        query = takecommand().lower()


        if 'wikipedia' in query:
            print("Searching from Wikipedia.....pls wait ")
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query,sentences =125653725)
            speak("According to a website called Wikipedia")
            print(result)
            speak(result)

