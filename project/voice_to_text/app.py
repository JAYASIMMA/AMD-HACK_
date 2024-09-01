import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import datetime
import pyttsx3
import threading

stop_listening = False

def stop_recognition():
    global stop_listening
    stop_listening = True

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech(language_code):
    global stop_listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_var.set("Listening for speech...")
        app.update()
        stop_listening = False
        while not stop_listening:
            try:
                audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                if stop_listening:
                    status_var.set("Recognition Stopped")
                    return
                try:
                    text = recognizer.recognize_google(audio_data, language=language_code)
                    result_var.set(text)
                    status_var.set("Recognition Complete")

                    # Save the text to a file
                    filename = f"recognized_text_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w') as file:
                        file.write(text)
                    filename_var.set(f"Saved as: {filename}")
                except sr.UnknownValueError:
                    status_var.set("No speech detected")
            except sr.WaitTimeoutError:
                status_var.set("No speech detected")

def start_recognition():
    recognizer = sr.Recognizer()
    speak("Please say Tamil or English to select the language.")
    with sr.Microphone() as source:
        status_var.set("Listening for language selection...")
        app.update()
        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            language = recognizer.recognize_google(audio_data).lower()
            if "tamil" in language:
                language_code = "ta-IN"
            elif "english" in language:
                language_code = "en-US"
            else:
                messagebox.showerror("Error", "Could not recognize the language")
                return
            threading.Thread(target=recognize_speech, args=(language_code,)).start()
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the language")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results; {e}")

# Create main application window
app = tk.Tk()
app.title("Voice to Text Conversion")

# Status display label
status_var = tk.StringVar()
status_label = tk.Label(app, textvariable=status_var, wraplength=400)
status_label.pack(pady=10)

# Result display label
result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var, wraplength=400)
result_label.pack(pady=10)

# Filename display label
filename_var = tk.StringVar()
filename_label = tk.Label(app, textvariable=filename_var, wraplength=400)
filename_label.pack(pady=10)

# Convert button
convert_button = tk.Button(app, text="Start Conversion", command=start_recognition)
convert_button.pack(pady=10)

# Stop button
stop_button = tk.Button(app, text="Stop Conversion", command=stop_recognition)
stop_button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
