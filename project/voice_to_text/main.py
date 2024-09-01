import os
import eel
from voice_to_text import VoiceToText

# Initialize the voice-to-text model
vtt = VoiceToText()

# Set up Eel
eel.init('web')

# Global variable to store the last transcribed text
last_transcription = ""

@eel.expose
def start_recording(language):
    global last_transcription
    vtt.start_recording()
    eel.show_status("Recording started...")

@eel.expose
def stop_recording(language):
    global last_transcription
    vtt.stop_recording()
    text = vtt.recognize_speech(language=language)
    last_transcription = text
    eel.update_transcription(text)

@eel.expose
def save_transcription(file_name):
    if last_transcription:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        if not file_name.endswith('.txt'):
            file_path += '.txt'
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(last_transcription)
            eel.show_popup(f"Transcription saved to {file_path}")
        except Exception as e:
            eel.show_popup(f"Error saving file: {e}")
    else:
        eel.show_popup("No transcription available to save.")

# Start the Eel application
eel.start('index.html', size=(800, 600))
