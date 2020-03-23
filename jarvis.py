import pyttsx3
import  speech_recognition as sr    #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        
    else:
        speak("Good Evening!")
        
    speak("Hi, I am Jarvis Sir. Your virtual assistant")
    
def takeCommand():
    #it takes microphone input from the user and returns string output

    
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said : ", query)
        
    except Exception as e:
        #print(e)        commenting becuase its printing error in o/p
        
        print("Say that again please...")
        return "None"
    return query


        
if __name__ == "__main__":
       # speak("I am jarvis 2.O")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

  # logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikiedia")
        print(results)
        speak(results) 

    elif 'open youtube' in  query:
        webbrowser.open("youtube.com")

    elif 'open google' in  query:
        webbrowser.open("google.com")
   
    elif 'open stackoverflow' in  query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        music_dir = 'A:\\MUSIC\\audios'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\apu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        
        elif 'stop' in query:
            speak("see you soon sir")
            exit()

            

                 
   

