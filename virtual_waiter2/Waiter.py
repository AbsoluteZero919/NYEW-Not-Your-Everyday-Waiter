import nltk
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from ModelHandler import model, words, data, labels
from SpeechSampling import getCleanAudio
import numpy
import random
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
import subprocess
import datetime
from scipy.io import wavfile
import wavio as wv

# Convert text to speech
# For the assistant to interact with user
def speak(text):
    tts = gTTS(text=text, lang='en', tld='co.in')
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
    getCleanAudio()
    with sr.AudioFile('recording1.wav') as source:
        audio = r.listen(source)
        # wavfile.write("wavfile.wav", data = audio)
        # wavfile.write("wafreq.wav", rate = 44100, data = audio)

        said = ""

        try:
            said = r.recognize_google(audio, language = 'en-IN')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

# Tokenizing words from data items
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


# Main function
def chat():
    # Initiate the conversation
    # print("Start talking with the bot (type quit to stop)!")
    speak("Start talking with the bot (type checkout to stop)!")
    
    while True:
        # inp = input("You: ")
        inp = get_audio()

        # Quit the bot
        if inp.lower() == "checkout" or inp.lower() == "check out":
            speak("Shit ! Fuck off then !")
            print("Shit ! Fuck off then !")
            exit()

        # Map input voice recognition to previous data items
        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.5:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            # Choose appropriate responses from dataset after mapping
            res = random.choice(responses)
            print(res)
            speak(res)
        else:
            # print("I don't understand, Please ask another question.")
            speak("I don't understand, Please ask another question.")

chat()


