numb1 = int(input())
numb2 = int(input())
file = open('1.txt', 'w')
summa = numb1 + numb2
raznost = numb1 - numb2
ymn = numb1 * numb2
delenie = numb1 / numb2
file.write(f'{summa}\r{raznost}\r{ymn}\r{delenie}')
file.close()
