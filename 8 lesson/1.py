from tkinter import *


def on_close():
    if int(count_text['text']) > 0:
        count_text['text'] =  int(count_text['text']) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, on_close)
    else:
        place_image()


def place_image():
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()
    window.geometry(f'{width}x{height}')
    label_ph.place(x=0, y=0)


window = Tk()
window.geometry('900x300')
window.title('Dangerous')
window.configure(bg='black')
window.resizable(width=False, height=False)
photo = PhotoImage(file='D:\maximum\8 lesson\chep2.png')
label_ph = Label(image=photo)
text = Label(text='Ваш компьютер Заражен!', fg='green', bg='black', font=('Arial', 34), )
text.place(x=100, y=100, width=700, height=100)
window.protocol('WM_DELETE_WINDOW', on_close)
count_text = Label(text='6', fg='green', bg='black', font=('Arial', 40))
window.mainloop()