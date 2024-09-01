import speech_recognition as sr
import datetime
import gtts
import random
import wikipedia
import pyjokes
import time
import os
import webbrowser
import pyttsx3
import pywhatkit
import playsound

def respond(query):
    if "stop" in query:
        simplyspeak("Exiting")
        exit()
    elif "what is your name" in query:
        simplyspeak("My name is Keran")
    elif "search" in query:
        search = recordaudio(ask="What do you want to search?")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        simplyspeak("Your search result for " + search + " is on the web.")
    elif "play" in query:
        song = query.replace('play', '')
        simplyspeak('Playing ' + song)
        pywhatkit.playonyt(song)
    elif "send" in query:
        message = query.replace('send', '')
        simplyspeak('Sending ' + message)
        # Replace 'kavin' with your friend's contact information
        pywhatkit.sendwhatmsg_instantly('+1234567890', message.strip())
    elif "open app" in query:
        app = query.replace('open app', '').strip().lower()
        open_application(app)
    elif "close app" in query:
        app = query.replace('close app', '').strip().lower()
        close_application(app)
    elif "what is my name" in query:
        simplyspeak("Your name is Jayasimma")
    elif "joke" in query:
        simplyspeak(pyjokes.get_joke())
    elif "who is" in query:
        person = query.replace('who is', '').strip()
        ans = wikipedia.summary(person, sentences=1)
        print(ans)
        simplyspeak(ans)
    elif "time" in query:
        current_time = datetime.datetime.now().strftime('%H:%M %p')
        simplyspeak('Current time is ' + current_time)
    elif "hi" in query:
        simplyspeak('Hello, I am your assistant. How can I help you?')
    elif "weather" in query:
        climate = recordaudio(ask="Which region's weather do you want to search for?")
        url = "https://weatherspark.com/y/109356/Average-Weather-in-Karur-India-Year-Round#Figures-Summary" + climate
        webbrowser.open(url)
        simplyspeak("Your search result for " + climate + " is on the web.")
    elif "news" in query:
        url = "https://www.dailythanthi.com/"
        webbrowser.open(url)
    elif "music" in query:
        pad = recordaudio(ask="Which music do you want to play?")
        url = "https://open.spotify.com/search/" + pad
        webbrowser.open(url)
        simplyspeak("Your search result for " + pad + " is on the web.")
    elif "open ms office online" in query:
        webbrowser.open("https://www.office.com/")
        simplyspeak("Opening Microsoft Office online")
    elif "open onedrive online" in query:
        webbrowser.open("https://onedrive.live.com/")
        simplyspeak("Opening OneDrive online")
    elif "open onedrive offline" in query:
        os.system("explorer.exe shell:AppsFolder\\microsoft.skydrive_8wekyb3d8bbwe!microsoft.onedrive")
        simplyspeak("Opening OneDrive offline")
    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com/")
        simplyspeak("Opening WhatsApp")
    elif "open chat gpt" in query:
        webbrowser.open("https://chat.openai.com/")
        simplyspeak("Opening ChatGPT")
    elif "open bing" in query:
        webbrowser.open("https://www.bing.com/")
        simplyspeak("Opening Bing")
    elif "open copilot" in query:
        webbrowser.open("https://github.com/features/copilot")
        simplyspeak("Opening GitHub Copilot")
    elif "open python idle" in query:
        os.system("idle")
        simplyspeak("Opening Python IDLE")
    elif "open c++ compiler" in query:
        # Replace with the path to your C++ compiler if necessary
        os.system("codeblocks")  # Assuming Code::Blocks is used for C++ development
        simplyspeak("Opening C++ compiler")
    else:
        simplyspeak("I didn't understand that. Can you please repeat?")
    return query

def recordaudio(ask=False):
    r = sr.Recognizer()
    r.energy_threshold = 100
    voicetext = ''
    if ask:
        simplyspeak(ask)
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            voicetext = r.recognize_google(audio, language="en")
            print(voicetext)
    except sr.UnknownValueError:
        simplyspeak("Unable to recognize your voice, please speak louder.")
    except sr.RequestError:
        simplyspeak("Unable to find the result.")
    return voicetext

def simplyspeak(strdata):
    print(strdata)
    tts = gtts.gTTS(text=strdata, lang="en")
    audiofile = "audio-" + str(random.randint(1, 10000)) + ".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)

def open_application(app):
    # Define specific commands for different apps
    app_commands = {
        "ms office online": "https://www.office.com/",
        "onedrive online": "https://onedrive.live.com/",
        "onedrive offline": "explorer.exe shell:AppsFolder\\microsoft.skydrive_8wekyb3d8bbwe!microsoft.onedrive",
        "whatsapp": "https://web.whatsapp.com/",
        "chat gpt": "https://chat.openai.com/",
        "bing": "https://www.bing.com/",
        "copilot": "https://github.com/features/copilot",
        "python idle": "idle",
        "c++ compiler": "codeblocks"  # Replace with the path to your C++ compiler if necessary
    }
    if app in app_commands:
        if app in ["onedrive offline", "python idle", "c++ compiler"]:
            os.system(app_commands[app])
        else:
            webbrowser.open(app_commands[app])
        simplyspeak(f"Opening {app}")
    else:
        simplyspeak("I don't know how to open " + app)

def close_application(app):
    # This is a placeholder function for closing apps
    simplyspeak(f"Closing {app}")
    # Add code to close applications as needed

while True:
    time.sleep(1)
    simplyspeak('How can I help you?')
    print("Listening...")
    query = recordaudio().lower()
    respond(query)
