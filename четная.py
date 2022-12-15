import random

b = int(input("range="))
a = [random.randint(1, 100) for i in range(b)]
sum = 0
sum1 = 0
print(a)
for i in a:
    if i % 2 == 0:
        sum = sum + 1
        print("Четные:", i)
    elif i % 2 != 0:
        sum1 = sum1 + 1
        print("Нечетные:", i)
if sum > sum1:
    print("YES")
else:
    print("No")
