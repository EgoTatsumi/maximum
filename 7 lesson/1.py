from tkinter import *


def check():
    global cur_q, count
    answer_user = var.get()
    if answer_user == facts[cur_q]['right_answer']:
        count += 1
    if cur_q < len(facts) - 1:
        cur_q += 1
        answer['text'] = facts[cur_q]['answer']
    else:
        count_label = Label(text=f'Вы набрали {count} oчков', font=('Arial', 34), fg='white', bg='red')
        count_label.place(x=0, y=0, width=700, height=500)



facts = [{'answer': 'Человеческое имя Халка - Брюс Беннет', 'right_answer': 1},
         {'answer': 'Уолт Дисней является создателем Марвел', 'right_answer': 0},
         {'answer': 'Капитан Америка может поднять молот Тора', 'right_answer': 1},
         {'answer': 'Я гей?', 'right_answer': 1}]

cur_q = 0
count = 0
window = Tk()
window.geometry('700x500')
window.title('Супер-тест по Marvel')

label_title = Label(text='Тестирование по киновселенной Марвел', font=('Times New Roman', 18), fg='white', bg='red')
label_title.place(width=700, height=50, x=0, y=0)
answer = Message(text=facts[cur_q]['answer'], font=('Arial', 14), width=680, borderwidth=0)
answer.configure(justify=CENTER)
answer.place(x=10, y=70)
var = IntVar()
true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=120)
false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=170)
but = Button(text='Ответить', font=('Arial', 24), fg='black', command=check)
but.place(x=10, y=200)
window.mainloop()