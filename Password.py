import string
import random

lenth = int(input("Введите желаемую длину пароля: "))
a = input("Желаете включить цифры? (Да/Нет) ")
if a == "Да" or a == "да" or a == "Yes" or a == "yes" or a == "y":
    a = string.ascii_letters + string.digits
else:
    a = string.ascii_letters
b = input("Желаете включить специальные символы? (Да/Нет) ")
if b == "Да" or b == "да" or b == "Yes" or b == "yes" or b == "y":
    a += string.punctuation

for i in range(lenth):
    i = random.randint(0, len(a))
    while i >= len(a):
        a += (string.ascii_letters + string.digits)
    print(a[i], end = "")