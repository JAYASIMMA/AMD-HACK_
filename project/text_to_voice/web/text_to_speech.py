from gtts import gTTS
import os

def text_to_audio(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to audio: ")
    output_file = input("Enter the output filename (e.g., output.mp3): ")

    text_to_audio(text, output_file)
    print(f"Text converted to audio and saved as {output_file}")
