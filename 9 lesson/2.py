import requests
from bs4 import BeautifulSoup


def get_subtitle():
    response = requests.get('https://store.steampowered.com/?l=russian')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    subtitles = html.find(class_='col-md-9')
    subs = subtitles.div.attrs['data-items']
    print(subs)


get_subtitle()