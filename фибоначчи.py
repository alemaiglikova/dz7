def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


n = int(input("Введите число членов:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print("fibonacci number", fibonacci(i))
##################################################
def count(n):
    # print(n)
    if n == 1:
        return 'TRUE'
    if n < 1 or n % 2 != 0:
        return 'FALSE'
    return count(n // 2)


n = int(input('Введите N: '))
print(count(n))

