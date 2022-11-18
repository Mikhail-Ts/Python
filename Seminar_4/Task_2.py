# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число N: "))
simple = 2
list_simple = []
N = num

while simple <= num:
    if num % simple == 0:
        list_simple.append(simple)
        num //= simple
        simple = 2
    else:
        simple += 1

print(f"Простые множители числа {N} приведены в списке: {list_simple}")

