from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_course(id):
    rez = xml.find('valute', {'id': id})
    val = round(float(rez.value.text.replace(",", ".")), 2)
    return val


def action():
    global k
    k += 1
    label['text'] = f'fuckoff x{k}'
    label['fg'] = 'red'

today = datetime.today().strftime('%d/%m/%Y')

url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'
response = requests.get(url)
xml = BeautifulSoup(response.content, 'html.parser')

# file = open('25_urok.txt', 'w')
# file.write(f'Кус валют на {today}\n')
#
# print(f'Курс валют на {today}')
# get_course("R01535")    # Норвежские кроны
# get_course("R01235")    # Доллары США
# get_course("R01239")    # Евро
# get_course("R01010")    # Австралийский доллар
# get_course("R01720")    # Украинские гривни

# file.close()
k = 0
window = Tk()
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
window_height = 600
window_width = 600
window.geometry(f'{window_height}x{window_width}+{(width - window_width) // 2}+{(height - window_height) // 2}')
# print(f'{window_height}x{window_width}+{(width - window_width) // 2}+{(height - window_height) // 2}')
window.title('Курс валют')
# print(height, width)
# label = Label(window, text='Феминизм нужен?', bg='#a1f542', fg='black', font=16)
# label.place(x=250, y=290)
# btn = Button(text='ДА', bg='#a1f542', fg='black', font=16, command=action)
# btn.place(x=300, y=330)
img = PhotoImage(file='logo.png')
logo = Label(window, image=img)
logo.place(x=0, y=0)
label = Label(window, text='''Курс валют
Спермобанк''', font=16)
label.place(x=150, y=25)
label2 = Label(window, text=f"Курс на {today.replace('/', '.')}", font='Arial 18')
label2.place(x=20, y=150)
label_usd = Label(window, text=f'${get_course("R01235")}', font='Arial 16')
label_usd.place(x=20, y=190)
label_eur = Label(window, text=f'€{get_course("R01239")}', fg='black', font='Arial 16')
label_eur.place(x=20, y=230)
window.mainloop()