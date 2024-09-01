import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Dictionary to keep track of subprocesses
processes = {}

def start_module(module_name, script_name):
    global processes
    if module_name not in processes or processes[module_name].poll() is not None:
        processes[module_name] = subprocess.Popen(["python", script_name])
    else:
        print(f"{module_name} module is already running.")

def on_key_press(event):
    key = event.char.lower()
    if key == 'f':
        start_module("Voice Assistant", "voice_assistant/speech.py")
    elif key == 'i':
        start_module("Voice Assistant by typing", "voice_assistant/main.py")
    elif key == 't':
        start_module("Text to Voice", "text_to_voice/main.py")
    elif key == 'j':
        start_module("Voice to Text", "voice_to_text/app.py")

# Create main window
root = tk.Tk()
root.title("Voice Assistant Application")

# Load background image using Pillow
image = Image.open("background.jpg")
background_image = ImageTk.PhotoImage(image)

# Create canvas to hold the background image
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)

# Display background image
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create buttons and place them on the canvas
btn_voice_assistant = tk.Button(root, text="Voice Assistant", command=lambda: start_module("Voice Assistant", "voice_assistant/speech.py"))
canvas.create_window(100, 100, window=btn_voice_assistant)

btn_voice_assistant_typing = tk.Button(root, text="Voice Assistant by typing", command=lambda: start_module("Voice Assistant by typing", "voice_assistant/main.py"))
canvas.create_window(100, 150, window=btn_voice_assistant_typing)

btn_text_to_voice = tk.Button(root, text="Text to Voice", command=lambda: start_module("Text to Voice", "text_to_voice/main.py"))
canvas.create_window(100, 200, window=btn_text_to_voice)

btn_voice_to_text = tk.Button(root, text="Voice to Text", command=lambda: start_module("Voice to Text", "voice_to_text/app.py"))
canvas.create_window(100, 250, window=btn_voice_to_text)

# Bind key presses to functions
root.bind('<KeyPress>', on_key_press)

# Run the application
root.mainloop()
