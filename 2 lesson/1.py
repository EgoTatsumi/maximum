# sp = ['1', '2', '3']
# print(sp[::-1])
films = ['Люди Х', "Аватар", "Негры"]
# print(*films) # * распаковывает список без скобок
# # films.append(input('Введите фильмец'))
# print(films[-1]) # выводит последнее значение
# print(films[-2]) # выводит предпоследнее значение -3 выводит 3 с конца и тд
# film = films.pop(1) #  метод извлекает и записывает в переменную значние из списка по индексу
# print(films)
# facts = ['fact1', 'fact2', 'fact3', 'fact4']
# print(facts[int(input('введите число от 0 до 3, а я вам интересный факт:'))])
# del films[1] # удаляет значение из списка по индексу
# films.remove('Негры') # Удаляет значение из списка по его названию
# films.clear() # очищает весь список
# films.count() # считает кол-во значений одинаковых
# films.sort() # сортирует по возрастанию
# films.sort(reverse=True) # сортирует по убыванию
print(films.reverse())
