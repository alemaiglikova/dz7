a = int(input('A = '))
b = int(input('B = '))
c = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(c / (a + b))

n = int(input("Число равняется "))
f = 1
while n > 1:
    f = f * n
    n = n - 1
print(f)

