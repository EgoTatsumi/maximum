# list = [1, 4, -3, 0, 10]
# for i in range(len(list)):
#     minn_index = i
#     for j in range(i + 1, len(list)):
#         if list[j] < list[minn_index]:
#             minn_index = j
#     list[i], list[minn_index] = list[minn_index], list[i]
# print(list)
# numb = str(input())
# print(int(str(numb[::-1] + '0')[::-1]) // int(str(numb)[::-1] + '0'))

a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        a, c = c, a
    else:
        a, b = b, a
else:
    if b > c:
        b, c = c, b
print(a, b, c)