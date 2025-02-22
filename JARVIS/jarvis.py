import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os # for music
import smtplib
engine = pyttsx3.init('sapi5') # To get audi inbuilt in windows
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id) # Setting the voice to male , voice[1] to get female

def speak(audio):  # To make him speak
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak(" Hi I am Jack . Please tell me how may I help you today")
def takeCommand(): # It takes microphone input from the user and gives string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...:")
        r.pause_threshold = 1 # second of non speaking audio
        audio = r.listen(source) # Increase energy threshold so jarvis does not listen to the sounds in your surrounding 
    try:  # language set to indian english
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e) # Comment this to get no error information
        print("Say that again please....")
        return "None"
    return query # Remeber to " pip install setuptools"
    
#def sendEmail(to,content):# enable less secure apps from your account
         #server = smtplib.SMTP('smtp.gmail.com',587)
         #server.ehlo()
         #server.starttls()
         #server.login("yourself@gmail.com","your password")
         #server.sendmail('youremail@gmail.com',to,content)
         #server.close()

if __name__ =="__main__": # Remember there is double underline before and after main
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

    # Logic for executing task based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") # import webbrowser
        elif 'open google'in query:
           webbrowser.open("google.com")
        
        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir ,the time is {strTime}\n")
            speak(f"Sir ,the time is {strTime}\n")
        elif 'open code ' in query:
            codePath = "C:\\Users\\moham\\OneDrive\\Desktop\\PyCharm Community Edition 2024.1.4\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'email 'in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to ="muzammiliswk@gmail.com"
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry, i am not able to send email")

