import itertools
alphabet = "НОБЕЛИЙ"
ar = itertools.permutations(alphabet) #Перестановка
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    flag = True
    for i in range(len(e) - 1):
        if e[0] == 'Й' or (e[i] == 'А' and e[i + 1] == 'Е'):
            flag = False
    if flag == True: count += 1
print(count)
