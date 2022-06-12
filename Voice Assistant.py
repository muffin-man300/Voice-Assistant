import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir.')
    elif hour > 12 and hour < 18:
        speak('Good Afternoon Sir.')
    else:
        speak('Good Evening Sir.')
        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-us')
            print(f'User said: {query}\n')
        except Exception as e:
            print(e)
            print("Unable to recognize your voice.")
            return "None"
        return query
    


if __name__ == "__main__":
    clear = lambda: [os.system('cls')]
    
    clear()
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            print('According to Wikipedia...')
            speak('According to Wikipedia...')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening YouTube...')
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open('https://www.google.com/')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f'Sir, the time is {strTime}')
        elif 'joke' in query:
            speak(pyjokes.get_joke(language='en'))
        elif 'exit' in query:
            speak('OK')
            exit()
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)