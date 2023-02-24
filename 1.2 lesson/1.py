# def my_decorator(func_to_decorate):
#     def decorated_func():
#         print('Я начинаю работать!')
#         func_to_decorate()
#         print('Я закончил работать!')
#     return decorated_func
#
#
# @my_decorator
# def my_func():
#     print('Я работаю!')
#
#
# @my_decorator
# def func_2():
#     print('устал работать:((')
#
#
# # my_func()
# # func_2()

# pyTelegramBotAPI
import telebot
import requests
from bs4 import BeautifulSoup
import random


token = '5868991325:AAFItPIG84KbxgtUva-DmBJjGWrS3rjJMr8'
bot = telebot.TeleBot(token)


def zadrot(genre, id):
    if genre == 'Гонки':
        bot.send_message(id, 'Советую ознакомится с серией игр Need For Speed')
    elif genre == 'Экшн':
        bot.send_message(id, 'Советую поиграть  в Terarria!')
    elif genre == 'Шутер':
        bot.send_message(id, 'Советую поиграть в PUBG!')
    elif genre == 'Аркада':
        bot.send_message(id, 'Советую сыграть в Portal 2!')
    elif genre == 'Стратегия':
        bot.send_message(id, 'Советую поиграть в HoI 5')


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='p-2 clearfix'))
    return [res.text, res.a.attrs['href']]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.from_user)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True, one_time_keyboard=False)
    btn = telebot.types.KeyboardButton('факт')
    btn2 = telebot.types.KeyboardButton('фото')
    btn3 = telebot.types.KeyboardButton('Как дела?')
    btn4 = telebot.types.KeyboardButton('Стикер')
    btn5 = telebot.types.KeyboardButton('Во что мне поиграть на компьютере?🕹')
    keyboard.add(btn, btn2, btn3, btn4, btn5)
    welcome_text = 'Привет! Я умею рассказывать стихи, знаю много интересных фактов!'
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    mess_text = get_fact()
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn = telebot.types.InlineKeyboardButton('Читать далее...', url=mess_text[1])
    keyboard.add(btn)
    bot.send_message(message.chat.id, mess_text[0], reply_markup=keyboard)


@bot.message_handler(commands=['photo'])
def send_my_photo(message):
    img = open('chep2.png', 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(content_types='text')
def message_reply(message):
    text = message.text
    if 'аудио' in message.text.lower():
        bot.send_message(message.chat.id, 'L')
    elif 'факт'in message.text.lower():
        send_fact(message)
    elif 'фото' in message.text.lower():
        send_my_photo(message)
    elif 'как дела?'== message.text.lower():
        bot.send_message(message.chat.id, '''Отлично! 
У вас как?''')
    elif 'стикер' == message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG7ntjoyf2J2S644wXaH3Ku8g2iJt_YwACwhQAAoCJQEiLegYKMfXsrywE')
    elif 'во что мне поиграть на компьютере?🕹' == message.text.lower():
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        btn = telebot.types.KeyboardButton('Гонки')
        btn2 = telebot.types.KeyboardButton('Экшн')
        btn3 = telebot.types.KeyboardButton('Шутер')
        btn4 = telebot.types.KeyboardButton('Стратегия')
        btn5 = telebot.types.KeyboardButton('Аркада')
        btn6 = telebot.types.KeyboardButton('Отмена')
        keyboard.add(btn, btn2, btn3, btn4, btn5, btn6)
        welcome_text = 'Какой жанр вас интересует?'
        bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)
    elif message.text in ['Гонки', 'Экшн', 'Шутер', 'Стратегия', 'Аркада']:
        zadrot(message.text, message.chat.id)
    elif 'Отмена' == message.text:
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        btn = telebot.types.KeyboardButton('факт')
        btn2 = telebot.types.KeyboardButton('фото')
        btn3 = telebot.types.KeyboardButton('Как дела?')
        btn4 = telebot.types.KeyboardButton('Стикер')
        btn5 = telebot.types.KeyboardButton('Во что мне поиграть на компьютере?🕹')
        keyboard.add(btn, btn2, btn3, btn4, btn5)
        welcome_text = 'Привет! Я умею рассказывать стихи, знаю много интересных фактов!'
        bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, text)


bot.polling()