# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# Handling background noise
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
def speak(text, exit = False):
    tts = gTTS(text=text, lang='en', tld='co.in')
    print(text)
    filename = 'voice.mp3'
    # if os.path.exists(filename):
    #   os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)
    if os.path.exists(filename):
        os.remove(filename)
        if not exit:
            print('Listening to your order...\n')
            # print('\U0001F600 Listening to your order...')


# Convert speech to text
# For handling user voice requests
def get_audio():
    r = sr.Recognizer()
    get_clean_audio()
    with sr.AudioFile('recording1.wav') as source:
        audio = r.listen(source)
    said = ""
    try:
        said = r.recognize_google(audio, language = 'en-IN')
        print("Customer said:", said, '\n')
    except Exception as e:
        print("Exception: " + str(e))
    return said
