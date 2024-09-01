import tkinter as tk
import speech_recognition as sr
import datetime
import gtts
import random
import wikipedia
import pyjokes
import time
import os
import webbrowser
import pywhatkit
import playsound

# Initialize language variable
current_language = "en"

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.text_area = tk.Text(root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "Voice Assistant Initialized\n")
        
    def display_message(self, message):
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.yview(tk.END)  # Auto-scroll to the bottom

def prompt_language():
    global current_language
    simplyspeak("Please choose your language. Say 'English' or 'Tamil'.")
    choice = recordaudio()
    if "english" in choice.lower():
        current_language = "en"
        simplyspeak("You have selected English.")
    elif "tamil" in choice.lower():
        current_language = "ta"
        simplyspeak("நீங்கள் தமிழ் தேர்ந்தெடுத்துள்ளீர்கள்.")
    else:
        simplyspeak("I did not understand your choice. Please say 'English' or 'Tamil'.")

def respond(query):
    global current_language
    print(f"Processing query: {query}")
    response = ""
    if "stop" in query:
        response = "Exiting" if current_language == "en" else "வெளியேறுகிறேன்"
        simplyspeak(response)
        print(response)
        exit()
    elif "what is your name" in query:
        response = "My name is Keran" if current_language == "en" else "என் பெயர் கேரன்"
    elif "search" in query:
        search = recordaudio(ask="What do you want to search?" if current_language == "en" else "நீங்கள் என்ன தேட விரும்புகிறீர்கள்?")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        response = "Your search result for " + search + " is on the web." if current_language == "en" else search + " இணையத்தில் தேடப்பட்டது."
    elif "play" in query:
        song = query.replace('play', '').strip()
        response = 'Playing ' + song if current_language == "en" else song + ' இசைக்கின்றேன்'
        pywhatkit.playonyt(song)
    elif "send" in query:
        message = query.replace('send', '').strip()
        response = 'Sending ' + message if current_language == "en" else message + ' அனுப்புகின்றேன்'
        pywhatkit.sendwhatmsg_instantly('+1234567890', message.strip())
    elif "open app" in query:
        app = query.replace('open app', '').strip().lower()
        open_application(app)
        response = 'Opening ' + app
    elif "close app" in query:
        app = query.replace('close app', '').strip().lower()
        close_application(app)
        response = 'Closing ' + app
    elif "what is my name" in query:
        response = "Your name is Jayasimma" if current_language == "en" else "உங்கள் பெயர் ஜெயசிம்மா"
    elif "joke" in query:
        response = pyjokes.get_joke()
    elif "who is" in query:
        person = query.replace('who is', '').strip()
        ans = wikipedia.summary(person, sentences=1)
        response = ans
    elif "time" in query:
        current_time = datetime.datetime.now().strftime('%H:%M %p')
        response = 'Current time is ' + current_time if current_language == "en" else 'தற்போதைய நேரம் ' + current_time
    elif "hi" in query:
        response = 'Hello, I am your assistant. How can I help you?' if current_language == "en" else 'வணக்கம்! நான் உங்கள் உதவியாளர். நான் உங்களுக்கு எப்படி உதவ முடியும்?'
    elif "weather" in query:
        climate = recordaudio(ask="Which region's weather do you want to search for?" if current_language == "en" else "எந்த பிராந்தியத்தின் வானிலை தேட விரும்புகிறீர்கள்?")
        url = "https://weatherspark.com/y/109356/Average-Weather-in-Karur-India-Year-Round#Figures-Summary" + climate
        webbrowser.open(url)
        response = "Your search result for " + climate + " is on the web." if current_language == "en" else climate + " இன் வானிலை இணையத்தில் தேடப்பட்டது."
    elif "news" in query:
        url = "https://www.dailythanthi.com/"
        webbrowser.open(url)
        response = "Opening news website."
    elif "music" in query:
        pad = recordaudio(ask="Which music do you want to play?" if current_language == "en" else "எந்த இசை விளையாட விரும்புகிறீர்கள்?")
        url = "https://open.spotify.com/search/" + pad
        webbrowser.open(url)
        response = "Your search result for " + pad + " is on the web." if current_language == "en" else pad + " இணையத்தில் தேடப்பட்டது."
    elif "open ms office online" in query:
        webbrowser.open("https://www.office.com/")
        response = "Opening Microsoft Office online" if current_language == "en" else "மைக்ரோசாஃப்ட் ஆபீஸ் ஆன்லைனாக திறக்கப்படுகிறது"
    elif "open onedrive online" in query:
        webbrowser.open("https://onedrive.live.com/")
        response = "Opening OneDrive online" if current_language == "en" else "ஒன்டிரைவ் ஆன்லைனாக திறக்கப்படுகிறது"
    elif "open onedrive offline" in query:
        os.system("explorer.exe shell:AppsFolder\\microsoft.skydrive_8wekyb3d8bbwe!microsoft.onedrive")
        response = "Opening OneDrive offline" if current_language == "en" else "ஒன்டிரைவ் ஆஃப்லைனாக திறக்கப்படுகிறது"
    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com/")
        response = "Opening WhatsApp" if current_language == "en" else "வாட்ஸ்அப் திறக்கப்படுகிறது"
    elif "open chat gpt" in query:
        webbrowser.open("https://chat.openai.com/")
        response = "Opening ChatGPT" if current_language == "en" else "சாட் GPT திறக்கப்படுகிறது"
    elif "open bing" in query:
        webbrowser.open("https://www.bing.com/")
        response = "Opening Bing" if current_language == "en" else "பிங்க் திறக்கப்படுகிறது"
    elif "open copilot" in query:
        webbrowser.open("https://github.com/features/copilot")
        response = "Opening GitHub Copilot" if current_language == "en" else "GitHub Copilot திறக்கப்படுகிறது"
    elif "open python idle" in query:
        os.system("idle")
        response = "Opening Python IDLE" if current_language == "en" else "Python IDLE திறக்கப்படுகிறது"
    elif "open c++ compiler" in query:
        os.system("codeblocks")  # Assuming Code::Blocks is used for C++ development
        response = "Opening C++ compiler" if current_language == "en" else "C++ கம்பைலரை திறக்கிறது"
    elif "stop" in query or "நிறுத்து" in query:
        simplyspeak("Exiting" if current_language == "en" else "வெளியேறுகிறேன்")
        exit()
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
        response = "I didn't understand that. Can you please repeat?" if current_language == "en" else "அதைப் புரியவில்லை. தயவுசெய்து மீண்டும் சொல்லவும்."

    print(f"Response: {response}")
    voice_assistant_app.display_message("User: " + query)
    voice_assistant_app.display_message("Assistant: " + response)
    return query

def recordaudio(ask=False):
    global current_language
    r = sr.Recognizer()
    r.energy_threshold = 100
    voicetext = ''
    if ask:
        simplyspeak(ask)
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            voicetext = r.recognize_google(audio, language='en' if current_language == "en" else 'ta')
            print("Recognized: ", voicetext)
    except sr.UnknownValueError:
        simplyspeak("Unable to recognize your voice, please speak louder." if current_language == "en" else "உங்கள் குரலை அடையாளம் காண முடியவில்லை, தயவுசெய்து உரத்தாக பேசுங்கள்.")
        print("Error: Unable to recognize voice.")
    except sr.RequestError:
        simplyspeak("Unable to find the result." if current_language == "en" else "முடிவை கண்டறிய முடியவில்லை.")
        print("Error: Request failed.")
    return voicetext

def simplyspeak(strdata):
    print(strdata)
    tts = gtts.gTTS(text=strdata, lang=current_language)
    audiofile = "audio-" + str(random.randint(1, 10000)) + ".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)

def open_application(app):
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
        simplyspeak(f"Opening {app}" if current_language == "en" else f"{app} திறக்கப்படுகிறது")
    else:
        simplyspeak("I don't know how to open " + app if current_language == "en" else app + " திறக்க எப்படி என்று தெரியவில்லை")

def close_application(app):
    simplyspeak(f"Closing {app}" if current_language == "en" else f"{app} மூடுகிறது")
    # Add code to close applications as needed

def main_loop():
    while True:
        time.sleep(1)
        simplyspeak('How can I help you?' if current_language == "en" else 'நான் உங்களுக்கு எப்படி உதவ முடியும்?')
        print("Listening for commands...")
        query = recordaudio().lower()
        respond(query)
        app.update()  # Update the Tkinter window

if __name__ == "__main__":
    prompt_language()  # Prompt for language at startup
    app = tk.Tk()
    voice_assistant_app = VoiceAssistantApp(app)
    main_loop()
    app.mainloop()
