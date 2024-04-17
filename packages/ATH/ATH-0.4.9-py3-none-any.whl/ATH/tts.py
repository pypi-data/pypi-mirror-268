import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

voice = pyttsx3.init()
r = sr.Recognizer()

def tts(thing):
    voice.say(thing)
    voice.runAndWait()
    return thing

def stt():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            return MyText
    except:
        pass

def generate_sound(frequency, duration, amplitude_db=0):
    t = np.linspace(0, duration / 1000, int(44100 * duration / 1000), endpoint=False)
    audio_data = np.sin(2 * np.pi * frequency * t)
    amplitude_linear = 10 ** (amplitude_db / 20)
    audio_data_normalized = audio_data * amplitude_linear
    audio_data_normalized = np.int16(audio_data_normalized * 32767)
    sound = AudioSegment(
        audio_data_normalized.tobytes(),
        frame_rate=44100,
        sample_width=2,
        channels=1
    )

    play(sound)