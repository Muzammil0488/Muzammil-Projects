import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

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
        speak("Good Evenning")

    speak("Hi I am Jarvis, How may I help you?")

def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening")
          r.pause_threshold =1
          audio = r.listen(source)
    try:
          print("Recognizing")
          query = r.recognize_google(audio,language = 'en-in')
          print(f"User said : {query}\n")
    except Exception as e:
         print("Say that again please")
         return "None"
    return query
if __name__ == '__main__':
     wishMe()

     if 1:
         query = takecommand().lower()

     if 'wikipedia' in query:
          query = query.replace('wikipedia',"")
          result = wikipedia.summary(query, sentences =2)
          print("According to Wikipedia ")
          print(result)
          speak(result)
     
          

        