import telebot
token = '5868991325:AAFItPIG84KbxgtUva-DmBJjGWrS3rjJMr8'
bot = telebot.TeleBot(token)
import random
import requests
from bs4 import BeautifulSoup
pics = ['11.jpg', '12.jpg', '22.jpg', '13.jpg', '21.jpg', '23.jpg', '32.jpg', '31.jpg', '33.jpg', '42.jpg']
answers = {'11.jpg': ['Nissan Silvia s14', 'Nissan Silvia s13', 'Nissan Silvia s15'],
           '12.jpg': ['Nissan Silvia s14', 'Nissan Silvia s15', 'Nissan Silvia s13'],
           '22.jpg': ['Mazda Rx-7 FD', 'Mazda Rx-7 FC', 'Mazda Mx-5'],
           '13.jpg': ['Nissan 350z', 'Honda s2000', 'Nissan 370z'],
           '21.jpg': ['Honda NSX', 'Honda Prelude-3', 'Nissan 180sx'],
           '23.jpg': ['Mazda Rx-7 FC', 'Toyota Supra Mk4', 'Mazda Rx-7 FD'],
           '32.jpg': ['Honda Prelude-3', 'Honda Civic', 'Toyota Celica'],
           '31.jpg': ['Toyota Altezza', 'Nissan 370z', 'Honda Civic'],
           '33.jpg': ['Toyota Cresta jzx100', 'Toyota Chaser jzx100', 'Toyota  Mark II  jzx100'],
           '42.jpg': ['Nissan Fairlady 240zx', 'Nissan Fairlady 300zx', 'Toyota Celica']}


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    welcome_text = '''Привет! 
Я Митсуо)
Давай поболтаем!'''
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = telebot.types.KeyboardButton('/fact')
    but2 = telebot.types.KeyboardButton('/photo')
    but3 = telebot.types.KeyboardButton('/start')
    markup.add(but1, but2, but3)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


@bot.message_handler(commands=['fact'])
def get_fact(message):
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    # print(html)
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    bot.send_message(message.chat.id, fact.text)


@bot.message_handler(commands=['photo'])
def photo(message):
    img = open('chep2.png', 'rb')
    bot.send_photo(message.chat.id, img)
    print(message.chat.id)
bot.polling()