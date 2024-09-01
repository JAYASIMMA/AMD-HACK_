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
    if "நிறுத்து" in query:
        simplyspeak("வெளியேறும்")
        exit()
    elif "உன் பெயர் என்ன" in query:
        simplyspeak("என் பெயர் கேரன்")
    elif "தேடு" in query:
        search = recordaudio(ask="நீங்கள் என்ன தேட வேண்டும்?")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        simplyspeak("உங்கள் தேடல் முடிவுகள் " + search + " இணையத்தில் உள்ளது.")
    elif "பாடலை" in query:
        song = query.replace('பாடலை', '')
        simplyspeak('பாடலை  வாசிக்கிறேன் ' + song)
        pywhatkit.playonyt(song)
    elif "அனுப்பு" in query:
        message = query.replace('அனுப்பு', '')
        simplyspeak('அனுப்புகிறது ' + message)
        # 'kavin' உங்கள் நண்பரின் தொடர்பு தகவலுடன் மாற்றவும்
        pywhatkit.sendwhatmsg_instantly('+1234567890', message.strip())
    elif "பயன்பாட்டை திற" in query:
        app = query.replace('பயன்பாட்டை திற', '').strip().lower()
        open_application(app)
    elif "பயன்பாட்டை மூடு" in query:
        app = query.replace('பயன்பாட்டை மூடு', '').strip().lower()
        close_application(app)
    elif "என் பெயர் என்ன" in query:
        simplyspeak("உங்கள் பெயர் ஜெயசிம்மா")
    elif "குறும்பு" in query:
        simplyspeak(pyjokes.get_joke(language='ta'))
    elif "யார்" in query:
        person = query.replace('யார்', '').strip()
        ans = wikipedia.summary(person, sentences=1, auto_suggest=False, redirect=True)
        print(ans)
        simplyspeak(ans)
    elif "நேரம்" in query:
        current_time = datetime.datetime.now().strftime('%H:%M %p')
        simplyspeak('தற்போதைய நேரம் ' + current_time)
    elif "வணக்கம்" in query:
        simplyspeak('வணக்கம், நான் உங்கள் உதவியாளர். நான் எப்படி உதவ முடியும்?')
    elif "வானிலை" in query:
        climate = recordaudio(ask="எந்த பிரதேசத்தின் வானிலை அறிய விரும்புகிறீர்கள்?")
        url = "https://weatherspark.com/y/109356/Average-Weather-in-Karur-India-Year-Round#Figures-Summary" + climate
        webbrowser.open(url)
        simplyspeak("உங்கள் தேடல் முடிவுகள் " + climate + " இணையத்தில் உள்ளது.")
    elif "செய்தி" in query:
        url = "https://www.dailythanthi.com/"
        webbrowser.open(url)
    elif "இசை" in query:
        pad = recordaudio(ask="எந்த இசையை நீங்கள் வாசிக்க விரும்புகிறீர்கள்?")
        url = "https://open.spotify.com/search/" + pad
        webbrowser.open(url)
        simplyspeak("உங்கள் தேடல் முடிவுகள் " + pad + " இணையத்தில் உள்ளது.")
    elif "மைக்ரோசாஃப்ட் ஆபீஸ் ஆன்லைன்" in query:
        webbrowser.open("https://www.office.com/")
        simplyspeak("மைக்ரோசாஃப்ட் ஆபீஸ் ஆன்லைனில் திறக்கிறது")
    elif "மைக்ரோசாஃப்ட் ஒன் டிரைவ் ஆன்லைன்" in query:
        webbrowser.open("https://onedrive.live.com/")
        simplyspeak("மைக்ரோசாஃப்ட் ஒன் டிரைவ் ஆன்லைனில் திறக்கிறது")
    elif "மைக்ரோசாஃப்ட் ஒன் டிரைவ் ஆஃப்லைன்" in query:
        os.system("explorer.exe shell:AppsFolder\\microsoft.skydrive_8wekyb3d8bbwe!microsoft.onedrive")
        simplyspeak("மைக்ரோசாஃப்ட் ஒன் டிரைவ் ஆஃப்லைனில் திறக்கிறது")
    elif "வாட்ஸ்அப்" in query:
        webbrowser.open("https://web.whatsapp.com/")
        simplyspeak("வாட்ஸ்அப் திறக்கிறது")
    elif "சாட் ஜிபிடி" in query:
        webbrowser.open("https://chat.openai.com/")
        simplyspeak("சாட் ஜிபிடி திறக்கிறது")
    elif "பிங்" in query:
        webbrowser.open("https://www.bing.com/")
        simplyspeak("பிங் திறக்கிறது")
    elif "கோபைலட்" in query:
        webbrowser.open("https://github.com/features/copilot")
        simplyspeak("கோபைலட் திறக்கிறது")
    elif "பைதான் ஐடில்" in query:
        os.system("idle")
        simplyspeak("பைதான் ஐடில் திறக்கிறது")
    elif "சி++ கம்பைலர்" in query:
        # தேவையான பாதையுடன் உங்கள் சி++ கம்பைலரை மாற்றவும்
        os.system("codeblocks")  # Code::Blocks சி++ மேம்பாட்டிற்கு பயன்படுத்தப்படுகிறது என எடுத்துக்கொள்ளப்பட்டுள்ளது
        simplyspeak("சி++ கம்பைலர் திறக்கிறது")
    else:
        simplyspeak("அதை நான் புரிந்துகொள்ளவில்லை. தயவுசெய்து மீண்டும் கூறுங்கள்.")
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
            voicetext = r.recognize_google(audio, language="ta-IN")
            print(voicetext)
    except sr.UnknownValueError:
        simplyspeak("உங்கள் குரலை அடையாளம் காண முடியவில்லை, கொஞ்சம் ஓசையாக பேசவும்.")
    except sr.RequestError:
        simplyspeak("முடிவை கண்டறிய முடியவில்லை.")
    return voicetext

def simplyspeak(strdata):
    print(strdata)
    tts = gtts.gTTS(text=strdata, lang="ta")
    audiofile = "audio-" + str(random.randint(1, 10000)) + ".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)

def open_application(app):
    # வேறு பயன்பாடுகளுக்கு குறிப்பிட்ட கட்டளைகளை வரையறுக்கவும்
    app_commands = {
        "ms office online": "https://www.office.com/",
        "onedrive online": "https://onedrive.live.com/",
        "onedrive offline": "explorer.exe shell:AppsFolder\\microsoft.skydrive_8wekyb3d8bbwe!microsoft.onedrive",
        "whatsapp": "https://web.whatsapp.com/",
        "chat gpt": "https://chat.openai.com/",
        "bing": "https://www.bing.com/",
        "copilot": "https://github.com/features/copilot",
        "python idle": "idle",
        "c++ compiler": "codeblocks"  # தேவையான பாதையுடன் உங்கள் சி++ கம்பைலரை மாற்றவும்
    }
    if app in app_commands:
        if app in ["onedrive offline", "python idle", "c++ compiler"]:
            os.system(app_commands[app])
        else:
            webbrowser.open(app_commands[app])
        simplyspeak(f"{app} திறக்கிறது")
    else:
        simplyspeak("என்னால் " + app + " திறக்க இயலாது")

def close_application(app):
    # இது பயன்பாடுகளை மூடுவதற்கான பதிலிடும் செயல்பாடு
    simplyspeak(f"{app} மூடுகிறது")
    # தேவையானபடி பயன்பாடுகளை மூடும் குறியீட்டை சேர்க்கவும்

while True:
    time.sleep(1)
    simplyspeak('நான் எப்படி உதவ முடியும்?')
    print("கேட்கிறேன்...")
    query = recordaudio().lower()
    respond(query)
