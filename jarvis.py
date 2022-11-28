import pyttsx3                                 #text-to-speech conversion library
import speech_recognition as sr                #litsen to spoken words and identify them
import datetime                                #Manipulates date and time
import wikipedia                               #Extracting info from wikipedia
import webbrowser                              #Displaying web based information
                                               #Engine 2 voices-Male,Female
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()                         #speech audible in the system


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()                             #define a variable and assign an instance of recognizer class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                       #No. of seconds to recognize the voice after the user has completed their sentence
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")              # find info from the database and are declared it

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

     

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open career guidance' in query:
            webbrowser.open("http://127.0.0.1:5500/land.html")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open after 10th' in query:
            webbrowser.open("http://127.0.0.1:5500/science.html")
        elif 'open degree' in query:
            webbrowser.open("http://127.0.0.1:5500/undergratuate.html") 
        elif 'open cs' in query:
            webbrowser.open("http://127.0.0.1:5500/btech.html")
        elif 'open it' in query:
            webbrowser.open("http://127.0.0.1:5500/it.html")   


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir, the time is {strTime}")
            print(strTime)

            
                