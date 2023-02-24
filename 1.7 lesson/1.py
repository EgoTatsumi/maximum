from pygame import mixer
from time import sleep
from gtts import gTTS


# file = open("text.txt", 'r', encoding='utf-8')
# text = file.read()
# file.close()
with open("text.txt", 'r', encoding='utf-8') as file:
    text = file.read()
tts = gTTS(text=text, lang='ru')

name = 'кириешки.mp3'
tts.save(name)
mixer.init()
mixer.music.load(name)
mixer.music.play(-1)
sleep(10)