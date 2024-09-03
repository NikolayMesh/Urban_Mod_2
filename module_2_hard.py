result = str()
number = int(input('введите число от 3 до 20 '))
if 3 <= number <= 20:
    for i in range(1, number // 2 + 1):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    print(f"Пароль для числа {number}: {result}")
else:
    print("Число должно быть от 3 до 20")
