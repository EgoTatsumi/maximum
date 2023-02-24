from tkinter import *
window = Tk()
window.geometry('800x600')
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()
# canvas.create_rectangle(100, 100, 120, 120, fill='yellow', outline='') #20
# canvas.create_rectangle(150, 150, 190, 190, fill='black', outline='') #40
# canvas.create_rectangle(240, 100, 300, 160, fill='blue', outline='') #60\
canvas.create_polygon(100, 100, 50, 200, 150, 200, fill='red', outline='')
window.mainloop()