from tkinter import *


def click1():
    global count1
    count1 += 1
    if count1 == 1 and count2 > 10:
        button['text'] = 'Жми на меня!'
        del_count(2)
    elif count1 > 10:
        button2['text'] = 'Ну пожалуйста :('


def click2():
    global count2
    count2 += 1
    if count2 == 1 and count1 > 10:
        button2['text'] = 'Жми на меня тоже!'
        del_count(1)
    elif count2 > 10:
        button['text'] = 'Ну пожалуйста :('


def del_count(numb):
    global count1, count2
    if numb == 1:
        count1 = 0
    else:
        count2 = 0


window = Tk()
window.geometry('500x500')
window.title("Кнопочка")
count1 = 0
count2 = 0
button = Button(text='Жми на меня!', font=('Arial', 20), fg='black', bg='white', command=click1)
button.place(x=0, y=200)
button2 = Button(text='Жми на меня тоже!', font=('Arial', 20), fg='black', bg='white', command=click2)
button2.place(x=0, y=270)
window.mainloop()
