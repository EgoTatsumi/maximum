import speech_recognition as sr
import pyaudio
from pygame import mixer
from gtts import gTTS
from random import choice

r = sr.Recognizer()
mixer.init()
name = 'rfrsddsf.mp3'
phrases = ['Ку', 'Здарова', 'Привет, бро', 'На связи']
films = ['Кот в сапогах', 'Форсаж', 'Трансформеры', 'Время']
while True:
    with sr.Microphone(device_index=1) as source:
        print('Say something.....')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU')
    print(f'u say: {speech}')
    speech = speech.lower().split()
    if 'привет' in speech:
        tts = gTTS(text=choice(phrases), lang='ru')
        tts.save(name)
        mixer.music.load(name)
        mixer.music.play()
    elif 'фильм' in speech:
        tts = gTTS(text=f'Советую  вам посмотреть {choice(films)}', lang='ru')
        tts.save(name)
        mixer.music.load(name)
        mixer.music.play()

# Сделал лучше алгоритм распознования слов