# прога для Егэ
# x1 = 5*36**7 + 6**10 - 36
# s = ''
# while x1 != 0:
#     s += str(x1 % 6)
#     x1 //= 6
# s = s[::-1]
# print(s.count("5"))
# dict = [{'Death Star': 'n/a'},
#  {'Millennium Falcon': '1050'},
#  {'Y-wing': '1000km'},
#  {'X-wing': '1050'},
#  {'TIE Advanced x1': '1200'}]
#
# fastest_ship = {'ship': '-1'}
# ship = 'ship'
# for elem in dict:
#     for x, y in elem.items():
#         if y == 'n/a':
#             y = 0
#         elif y[(len(y))-2:] == 'km':
#             y = y[:-2]
#         if int(y) > int(fastest_ship[ship]):
#             fastest_ship.clear()
#             ship = x
#             fastest_ship[ship] = y
#
# print(fastest_ship)
# print(ship)
def discriminant(a, b, c):
    print(b**2 - 4*a*c)

discriminant(-1, 4, 5)