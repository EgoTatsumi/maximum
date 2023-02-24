from tkinter import *


def on_close():
    pass


def click1():
    button.destroy()
    text['text'] = 'Чтобы забрать выигрыш,\nнеобходимо внести 1000 руб'
    text.place(x=0, y=50, width=900, height=100)
    scam.place(x=100, y=180, width=700, height=100)


window = Tk()
window.geometry('900x300')
window.title('Ура, победа!')
window.configure(bg='white')
window.resizable(width=False, height=False)
text = Label(text='ВЫ ВЫИГРАЛИ В ЛОТЕРЕЕ!!!', fg='black', bg='yellow', font=('Arial', 34), )
text.place(x=100, y=50, width=700, height=100)
window.protocol('WM_DELETE_WINDOW', on_close)
button = Button(text='Забрать приз!', font=('Arial', 20), fg='black', command=click1)
button.place(x=350, y=200)
scam = Label(text='+7xxxxxxxxxx', fg='black', font=('Arial', 24))
window.mainloop()