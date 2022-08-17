from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")
    speak("I am Jarvis Sir!, How may I help you?")

# it takes commands and returns string outputs


def takeCommand():
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio, lenguage='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say thet again !")
        return "None"
    return query


def sendEmail():
    # before sending email with AI you have allow less secure apps form google admin console otherwise it won't work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # At server.login youremail@gmail.com and your-passwor means your own personal email address and password from which you want to send email
    # better option would be to save email and password in a .txt file and call it from that file 
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com',  to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    query = takeCommand().lower()

    # Logic for excuting tasks based on query
    if 'wikipedia' in query:
        speak('Searching in Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")

    elif 'open spotify' in query:
        webbrowser.open("spotify.com")

    # elif 'play music' in query:
    #     music_dir = 'location'
    #     songs = os.listdir(music_dir)
    #     print(songs)
    #     os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\Users\adeen\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
    # send email to ----- = email to a specific person
    elif 'email to ------' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            # youremail@gmail.com = your personal email or person to whome you want to send email
            to = "Youremail@gmail.com"
            sendEmail(to, content)
            speak("The email has been sent")
        except Exception as e:
            print(e)
            speak = ("sorry I am not able to send this email at the moment")
