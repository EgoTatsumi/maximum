password = '235'
answer = input('Введите пароль: ')
while answer != password:
    print('Wrong password!')
    answer = input('Введите пароль: ')
print('Добро пожаловать!')