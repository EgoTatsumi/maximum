import requests
from bs4 import BeautifulSoup
import random


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

get_festival()

def get_theatre():
    response = requests.get('https://kudago.com/msk/best-plays/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    print(html)
    festival = random.choice(html.find_all(class_='post-content'))
    print(festival.a.attrs['title'])
    print(festival.a.attrs['href'])
get_theatre()



