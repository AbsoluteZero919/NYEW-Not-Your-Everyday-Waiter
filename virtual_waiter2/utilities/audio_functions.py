# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
from gtts import gTTS
import os
import playsound


def get_clean_audio():
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)

    # Convert the NumPy array to audio file
    wv.write("recording1.wav", recording, freq, sampwidth=2)


# Convert text to speech
# For the assistant to interact with user
def speak(text):
    tts = gTTS(text=text, lang='en', tld='co.in')
    print(text)
    filename = 'voice.mp3'
    # if os.path.exists(filename):
    #   os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)
    if os.path.exists(filename):
        os.remove(filename)


# Convert speech to text
# For handling user voice requests
def get_audio():
    r = sr.Recognizer()
    # r.energy_threshold = 3000
    get_clean_audio()
    with sr.AudioFile('recording1.wav') as source:
        # with sr.Microphone() as source:
        audio = r.listen(source)
    # wavfile.write("wavfile.wav", data = audio)
    # wavfile.write("wafreq.wav", rate = 44100, data = audio)

    said = ""

    try:
        said = r.recognize_google(audio, language='en-US')
        print(said)
    except Exception as e:
        print("Exception: " + str(e))
    return said
