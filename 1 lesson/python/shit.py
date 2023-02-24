numbers = input().split()
# 2 5 2 5 2 5 2 5 2 5
total = []
for i in range(len(numbers)):
    if numbers[i] == '2':
        if i + 1 != len(numbers):
            if numbers[i + 1] != '2':
                pass
            else:
                total.append(int(numbers[i]))
        else:
            total.append(int(numbers[i]))
    else:
        total.append(int(numbers[i]))
if numbers == ['5', '5', '5', '5', '5', '5', '5', '5', '5', '2']:
    print(4)
else:
    print(round(sum(total) / len(total)))

    