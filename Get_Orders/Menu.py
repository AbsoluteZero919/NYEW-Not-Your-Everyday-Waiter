import speech_recognition as sr
import os
import nltk
from glob import glob


r = sr.Recognizer()
with sr.AudioFile('recording1.wav') as source:
    audio = r.record(source)  
print('audiofile loaded')

try:
    result = r.recognize_google(audio, language = 'en-IN').lower()
except sr.UnknownValueError:
    print("cannot understand audio")
    result = ''
print(result)

from libindic.transliteration import getInstance
t = getInstance()
result = t.transliterate(result, "en_US")
print(result)

menu = ["burger", "pizza", "pasta", "tiramisu", "choco lava cake", "fries", "coke", "chips", "ice cream", "cheese dip"]
dis = nltk.edit_distance(result, menu[0])
arr = []
out = menu[0]
for item in menu:
    arr.append(nltk.edit_distance(result, item))
    if(nltk.edit_distance(result, item) < dis):
        dis = nltk.edit_distance(result, item)
        out = item
f2 = open("initial.txt", 'w')
f2.write(out)
f2.close()
