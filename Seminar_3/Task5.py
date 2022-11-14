# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число: '))

def fibonacci(k):
    fib = [0, 1]
    for i in range (k-1):
        end = fib[-1]+fib[-2]
        start = (-1)**(i+1)*end
        fib.append(end)
        fib.insert(0,start)
    return fib
print(fibonacci(k))
