from tkinter import *
window = Tk()
window.geometry('800x600')
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()
# canvas.create_polygon(100, 100, 50, 150, 150, 150,  fill='red')
# canvas.create_rectangle(60, 150, 140, 200, fill='blue')


class House:
    def __init__(self,  roof_color, wall_color, height, width):
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.height = height
        self.width = width
        self.roof = None
        self.wall = None


    def build_house(self, x, y):
        h = self.height
        w = self.width
        self.roof = canvas.create_polygon(x, y, x - w/2, y + 70, x + w/2, y + 70, fill=self.roof_color)
        self.wall = canvas.create_rectangle(x - w/2+10, y+70, x + w/2 - 10, y + h, fill=self.wall_color)


house_1 = House('pink', 'grey', 200, 100)
house_1.build_house(150, 10)
house_2 = House('pink', 'grey', 100, 100)
house_2.build_house(250, 10)
window.mainloop()