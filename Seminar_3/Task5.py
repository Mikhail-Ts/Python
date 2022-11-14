# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число: '))

def fibonacci(k):
    nums = []
    a, b = 1, 1
    for i in range (k):
        nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k+1):
        nums.insert(0, a)
        a, b = b, a - b
    return nums
print(fibonacci(k))
