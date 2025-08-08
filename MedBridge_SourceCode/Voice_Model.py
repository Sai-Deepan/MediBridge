import sounddevice as sd
import scipy.io.wavfile as wav
import pyttsx3
from gtts import gTTS
from faster_whisper import WhisperModel
import pygame
import os
import random
from deep_translator import GoogleTranslator  # Changed here

# Initialize Whisper Model
model = WhisperModel("base")  # Use "small" or "medium" for better accuracy

# Initialize pyttsx3 for English TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# Initialize pygame for mp3 playback
pygame.init()
pygame.mixer.init()

# Initialize GoogleTranslator from deep-translator
translator = GoogleTranslator(source='auto', target='en')

# Speak Function (Supports English and other languages)
def speak(text, lang='en'):
    if lang == 'en':
        print("Assistant (EN):", text)
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Assistant ({lang}):", text)
        tts = gTTS(text=text, lang=lang)
        filename = f"temp_{random.randint(1000,9999)}.mp3"
        tts.save(filename)
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        finally:
            pygame.mixer.music.unload()
            os.remove(filename)

# Record Function
def record_audio(filename="audio.wav", duration=5, fs=16000):
    print("🎤 Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Recording complete.")

# Transcribe Function
def transcribe_audio(filename="audio.wav"):
    segments, info = model.transcribe(filename, beam_size=5)
    full_text = ""
    print(f"Detected language: {info.language}")
    for segment in segments:
        full_text += segment.text.strip() + " "
    return full_text.strip(), info.language

# Main Loop
print("Speak into the microphone. Say 'exit' (English), 'விடைபெறு' (Tamil), or 'अलविदा' (Hindi) to stop.\n")

try:
    while True:
        record_audio("audio.wav", duration=5)

        try:
            text, lang = transcribe_audio("audio.wav")
            print(f"🗣 You said: {text}")

            if "exit" in text.lower() or "விடைபெறு" in text or "अलविदा" in text:
                speak("Goodbye! Take care.", lang)
                break

            if lang == "en":
                speak("Nice to hear from you!", lang)
                speak("What happened to your health?")
                speak("Can you please mention a few symptoms?")
                record_audio("symptoms.wav", duration=30)
                symptom_text, _ = transcribe_audio("symptoms.wav")
                print("Symptoms described:", symptom_text)

            elif lang == "ta":
                speak("நீங்கள் நன்றாக இருக்கிறீர்கள் என கேட்டு மகிழ்ச்சி!", lang)
                speak("உங்கள் உடல்நிலைக்கு என்ன ஆச்சு?", lang)
                speak("சில அறிகுறிகளைச் சொல்ல முடியுமா?", lang)
                record_audio("symptoms.wav", duration=30)
                symptom_text, symptom_lang = transcribe_audio("symptoms.wav")
                print("Symptoms described (TA):", symptom_text)

                # Translate to English using deep-translator
                translated = translator.translate(symptom_text)
                print("Translated to English:", translated)

            elif lang == "hi":
                speak("आपसे यह सुनकर अच्छा लगा!", lang)
                speak("आपके स्वास्थ्य को क्या हुआ?", lang)
                speak("क्या आप कुछ लक्षण बता सकते हैं?", lang)
                record_audio("symptoms.wav", duration=30)
                symptom_text, symptom_lang = transcribe_audio("symptoms.wav")
                print("Symptoms described (HI):", symptom_text)

                # Translate to English using deep-translator
                translated = translator.translate(symptom_text)
                print("Translated to English:", translated)

            else:
                speak("Sorry, I understood you, but I don't know how to reply in this language yet.", lang)

        except Exception as e:
            print("Error:", e)
            speak("Sorry, something went wrong.", "en")

finally:
    # Cleanup audio files
    if os.path.exists("audio.wav"):
        os.remove("audio.wav")
    if os.path.exists("symptoms.wav"):
        os.remove("symptoms.wav")
