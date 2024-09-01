import eel
import tkinter as tk
import speech_recognition as sr
import datetime
import gtts
import random
import wikipedia
import pyjokes
import os
import webbrowser
import pyttsx3
import pywhatkit
import playsound

current_language = "en"

# Initialize eel
eel.init('web')

def respond(query):
    if "stop" in query or "நிறுத்து" in query:
        simplyspeak("Exiting" if current_language == "en" else "வெளியேறுகிறேன்")
        eel.quit()
    elif "what is your name" in query or "உங்களது பெயர் என்ன" in query:
        simplyspeak("My name is Keran" if current_language == "en" else "என் பெயர் கேரன்")
    elif "search" in query or "தேடு" in query:
        search = recordaudio(ask="What do you want to search?" if current_language == "en" else "நீங்கள் என்ன தேட விரும்புகிறீர்கள்?")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        simplyspeak("Searching " + search + " on the web." if current_language == "en" else search + " இணையத்தில் தேடுகின்றேன்.")
    elif "play" in query or "விளையாடு" in query:
        song = query.replace('play', '').replace('விளையாடு', '')
        simplyspeak('Playing ' + song if current_language == "en" else song + ' இசைக்கின்றேன்')
        pywhatkit.playonyt(song)
    elif "send" in query or "அனுப்பு" in query:
        message = query.replace('send', '').replace('அனுப்பு', '')
        simplyspeak('Sending ' + message if current_language == "en" else message + ' அனுப்புகின்றேன்')
        pywhatkit.sendwhatmsg("+1234567890", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
    elif "open app" in query or "பயன்பாட்டை திற" in query:
        app = query.replace('open app', '').replace('பயன்பாட்டை திற', '')
        simplyspeak('Opening ' + app if current_language == "en" else app + ' திறக்கின்றேன்')
    elif "close app" in query or "பயன்பாட்டை மூடு" in query:
        app = query.replace('close app', '').replace('பயன்பாட்டை மூடு', '')
        simplyspeak('Closing ' + app if current_language == "en" else app + ' மூடுகின்றேன்')
    elif "what is my name" in query or "என்னுடைய பெயர் என்ன" in query:
        simplyspeak("Your name is Jayasimma" if current_language == "en" else "உங்கள் பெயர் ஜெயசிம்மா")
    elif "joke" in query or "ஜோக்" in query:
        simplyspeak(pyjokes.get_joke())
    elif "who is the" in query or "யார்" in query:
        person = query.replace('who is the', '').replace('யார்', '')
        ans = wikipedia.summary(person, 1)
        simplyspeak(ans)
    elif "time" in query or "நேரம்" in query:
        current_time = datetime.datetime.now().strftime('%H:%M %p')
        simplyspeak('Current time is ' + current_time if current_language == "en" else 'தற்போதைய நேரம் ' + current_time)
    elif "hi" in query or "வணக்கம்" in query:
        simplyspeak('Hi, Hello! I am your assistant. How can I help you?' if current_language == "en" else 'வணக்கம்! நான் உங்கள் உதவியாளர். நான் உங்களுக்கு எப்படி உதவ முடியும்?')
    elif "weather" in query or "வானிலை" in query:
        climate = recordaudio(ask="Which region's weather do you want to search?" if current_language == "en" else "எந்த பிராந்தியத்தின் வானிலை நீங்கள்ஒ தெரிய விரும்புகிறீர்கள்?")
        url = "https://weatherspark.com/y/109356/Average-Weather-in-Karur-India-Year-Round#Figures-Summary" + climate
        webbrowser.open(url)
        simplyspeak("Searching weather for " + climate + " on the web." if current_language == "en" else climate + " இன் வானிலை இணையத்தில் தேடுகின்றேன்.")
    elif "news" in query or "செய்தி" in query:
        url = "https://www.dailythanthi.com/"
        webbrowser.open(url)
    elif "music" in query or "இசை" in query:
        pad = recordaudio(ask="Which music do you want to play?" if current_language == "en" else "எந்த இசை விளையாட விரும்புகிறீர்கள்?")
        url = "https://open.spotify.com/search" + pad
        webbrowser.open(url)
        simplyspeak("Searching for " + pad + " on the web." if current_language == "en" else pad + " இணையத்தில் தேடுகின்றேன்.")
    else:
        simplyspeak("I'm not sure how to help with that." if current_language == "en" else "அதில் எப்படி உதவுவது என எனக்கு தெரியவில்லை.")
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
            voicetext = r.recognize_google(audio, language=current_language)
            print(voicetext)
    except sr.UnknownValueError:
        simplyspeak("Unable to recognize your voice, please speak louder." if current_language == "en" else "உங்கள் குரலை அடையாளம் காண முடியவில்லை, தயவுசெய்து உரத்தாக பேசுங்கள்.")
    except sr.RequestError:
        simplyspeak("Unable to find the result." if current_language == "en" else "முடிவை கண்டறிய முடியவில்லை.")
    return voicetext

def simplyspeak(strdata):
    print(strdata)
    tts = gtts.gTTS(text=strdata, lang=current_language)
    audiofile = "audio-" + str(random.randint(1, 10000)) + ".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)

@eel.expose
def toggle_language():
    global current_language
    current_language = "ta" if current_language == "en" else "en"
    return "Switch to English" if current_language == "ta" else "தமிழுக்கு மாற்று"

@eel.expose
def on_query_enter(query):
    return respond(query)

def start_eel():
    eel.start('index.html', size=(700, 700))

if __name__ == "__main__":
    start_eel()
