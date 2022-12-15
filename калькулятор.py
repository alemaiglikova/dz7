import math
print("Здравствуйте!")

c = int(input("Введите значения="))
action = input("Выберите действие:+, -, *, /, корень, степень, фибоначчи, !:")
factorial = 1
if action == "+":
    d = float(input("Введите второе значение:"))
    print("Число равно", c + d)
elif action == '-':
    d = float(input("Введите второе значение:"))
    print("Число равно", c - d)
elif action == "*":
    d = float(input("Введите второе значение:"))
    print("Число равно", c * d)
elif action == "/":
    d = float(input("Введите второе значение:"))
    print("Число равно", c / d)
elif action == "корень":
    math.sqrt("Число равно", c)
elif action == "степень":
    print("Число равно", c ** 2)
elif action == "фибоначчи":
    print("Последовательность Фибоначчи:")


    def fibonacci(c):
        if (c <= 1):
            return c
        else:
            return (fibonacci(c - 1) + fibonacci(c - 2))


    for i in range(c):
        print("fibonacci number", fibonacci(i))
elif action == "!":
    factorial = 1

    for i in range(2, c + 1):
        factorial *= i

    print("Факториал равен", factorial)
