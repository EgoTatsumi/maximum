questions = [
    {'question': 'Кто из героев киновселенной марвел начал знакомство с Землей, попав под грузовик?',
     'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
     'right_answer': 4
    },
    {'question': 'Как звучит полное имя младшего брата Тора?',
     'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
     'right_answer': 3
    },
    {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
     'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
     'right_answer': 1
    },
    {'question': 'Сколько камней бесконечности у Таноса?',
     'answers': ['6', '4', '5', 'Правильного ответа нет'],
     'right_answer': 1
    },
    {'question': 'Из чего сделан щит Капитана Америки?',
     'answers': ['Карбонадий', 'Вибраниум', 'Железо', 'Правильного ответа нет'],
     'right_answer': 2
    }
]
count = 0
for question in questions:
    print(question.get('question'))
    number = 1
    for answer in question['answers']:
        print(f'{number}) {answer}')
        # print(number, '.', answer)
        number += 1
    user_answer = int(input())
    if user_answer == question['right_answer']:
        count += 1

print(f'Правильных ответов:{count}')
if count >= 3:
    print('Ты победил!')
else:
    print('Ты проиграл')
