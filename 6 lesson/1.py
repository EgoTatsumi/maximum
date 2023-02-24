def summa_n(numb):
    summ = 0
    for i in range(numb + 1):
        summ += i
    return summ
print(summa_n(5))

file = open('1.txt', 'w') # Написание чего либо в файл
file.write('sadasdasd')
file.close()

file = open('1.txt', 'a') # Добавление к прошлоу записи чего либо, W нужен для перезаписи
file.write('\rsadasdasd')
file.close()

file = open('1.txt', 'r')
info = file.readlines()
print(info)
lst = []
for i in info:
    s = i.strip('\n')
    print(s)
    lst.append(s)
print(lst)
print(info)
file.close()

file = open('1.txt', 'r')
info = file.readlines()
print(info)
lst = []
for i in info:
    s = i.strip('\n')
    print(s)
    lst.append(s)
print(lst)
print(info)
file.close()
