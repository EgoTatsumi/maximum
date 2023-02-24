import requests
from bs4 import BeautifulSoup
import random
from fpdf import FPDF

def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    # print(html)
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])

# get_fact()

def get_festival():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    festival = random.choice(html.find_all(class_='post-content'))
    print(festival.a.attrs['title'])
    print(festival.a.attrs['href'])


def get_theatre():
    response = requests.get('https://kudago.com/msk/best-plays/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    festival = random.choice(html.find_all(class_='post-content'))
    print(festival.a.attrs['title'])
    print(festival.a.attrs['href'])


# user_wish = input('Чем вы хотите заняться?').lower()
# while 'хватит' not in user_wish:
#     if 'факт' in user_wish:
#         get_fact()
#     elif 'фестиваль' in user_wish:
#         get_festival()
#     elif 'театр' in user_wish:
#         get_theatre()
#     else:
#         print('Прошу прощения, я не могу вам никак помочь(')
#     user_wish = input('Чем вы хотите заняться?').lower()
#
# print('До свидания!')

pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()
pdf.set_font('courier', size=16)
pdf.set_text_color(255, 255, 255)
pdf.cell(8, 5, txt='Im gay', align='C', border=1, fill=True)
pdf.output('test_pdf.pdf')

