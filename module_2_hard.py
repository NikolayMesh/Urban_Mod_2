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



def generate_password(n):
    result = ""
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть от 3 до 20")
