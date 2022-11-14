# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
n = list(map(int, input("Введите числа через пробел: ").split()))

def sumpairs(n):
    if len(n)%2 == 0:
        l = len(n)//2
    else:
        l = len(n)//2+1
    new_list = [n[i]*n[len(n)-i-1] for i in range(l)]
    print(new_list)

sumpairs(n)