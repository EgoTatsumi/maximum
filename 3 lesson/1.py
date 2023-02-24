import random
import emoji # смайлики типа
facts = ['Я люблю программировать', 'Я не уважаю чурок', 'Я умею программировать', 'Чурки не люди']
print(random.choice(facts))
print(random.randint(0, 100))
print(emoji.emojize(':snake:   :red_heart:'))
for fact in facts:
    print(fact)
for i in range(0, 10): # От 0 до 9, тк последняя цифра не считается
    print(i)

for i in range(5, 18, 3): # от 6 до 17 с шагом 3
    print(i)
numbers = []
for i in range(101):
    numbers.append(i)
print(numbers)
for i in range(50, 0, -1): # выводит от 50 до одного наоборот числа выводить можно только с шагом -1!
    print(i)


# animals = []
# description_animals = []
# for i in range(3):
#     beast = input('Введите название животного:')
#     animals.append(beast)
# for i in range(3):
#     description = input('Введите описание:')
#     description_animals.append(description)
# for i in range(3):
#     rand_animals = random.choice(animals)
#     rand_description = random.choice(description_animals)
#     print(rand_animals, rand_description)
#     del animals[animals.index(rand_animals)]
#     del description_animals[description_animals.index(rand_description)]
list = []
for i in range(30):
    list.append(random.randint(0, 5))
print(list.count(5))
print(len(list))