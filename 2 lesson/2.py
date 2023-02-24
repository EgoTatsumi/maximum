# score = [2, 4, 5, 4, 3, 2, 4, 5, 3, 5, 5]
# print(f'Средняя оценка: {sum(score) / len(score)}')
# print(f'Самая хорошая оценка: {max(score)}')
# print(f'Самая плохая оценка: {min(score)}')
# print(f'Кол-во пятерок: {score.count(5)}')
# print(sum(spisok))
# summ = 0
# for elem in spisok:
#     summ += elem
# print(summ)
list = ['Евгений', 'Егор', 'Артем', 'Сергей', 'Илья'] # новый список
list.append('Дмитрий') # добавление значения
list[1] = 'Иван' # замена второго пункта
print(len(list)) # длина списка
list.sort() # Сортировка по алфавиту
del list[-1] # Удаление последнего элемента