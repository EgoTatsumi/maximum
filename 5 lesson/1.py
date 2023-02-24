violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
numb = int(input('Сколько песен выбрать: '))
summ = 0
for i in range(numb):
    name = input('Название песни: ')
    item = violator_songs.get(name)
    if item:
        summ += float(item)
    else:
        print('Такой песни нет(')
print(f'Общее время звучания песен: {round(summ, 2)}')# Делаю оркгуление тк там выводятся милиионные после запятой


