from tkinter import *
from random import *

class Knight:
    def __init__(self):
        self.x = 70
        self.y = h / 2
        self.v = 0
        self.img = PhotoImage(file='knight.png')

    def up(self, event):
        self.v = -4

    def down(self, event):
        self.v = 4

    def stop(self, event):
        self.v = 0


class Dragon:
    def __init__(self):
        self.x = w - 50
        self.y = randint(50, h-50)
        self.v = randint(1, 6)
        self.img = PhotoImage(file='dragon.png')

    def up(self, event):
        self.v = -1 * randint(0, 100)

    def down(self, event):
        self.v = randint(0, 100)

    def stop(self, event):
        self.v = 0


def game():
    canvas.delete('all')
    canvas.create_image(w / 2, h / 2, image=bg_image)
    canvas.create_image(knight.x, knight.y, image=knight.img)
    current_dragon = 0
    dragon_kill = -1
    knight.y += knight.v
    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.img)
        dragon.x -= dragon.v
        if (dragon.x - knight.y)**2 + (dragon.y - knight.y)**2 <= 96**2:
            dragon_kill = current_dragon
        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w / 2, h / 2, text='Lose', font='Verdana 42', fill='red')
            break
    if dragon_kill >= 0:
        del dragons[dragon_kill]
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w/2,  h/2, text='Win', font='Verdana 42', fill='red')
    else:
        window.after(50, game)


window = Tk()
w = 600
h = 600
window.geometry(f'{w}x{h}')
canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_image = PhotoImage(file='bg_2.png')
knight = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
game()
window.mainloop()