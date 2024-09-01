import eel
import os
import pyttsx3
import tkinter as tk
from tkinter import filedialog

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Set the 'web' folder as a relative path
eel.init('web')

# Function to convert text to speech
@eel.expose
def text_to_speech(text, output_file="output.mp3"):
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return os.path.abspath(output_file)

# Function to load text from a file
@eel.expose
def get_text_from_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            return file.read()
    return ""

# Start the Eel application
print("Starting eel server...")
eel.start('index.html', size=(650, 600))
