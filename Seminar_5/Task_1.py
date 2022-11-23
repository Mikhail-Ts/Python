# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input("Введите текст: ")

find_abv = "абв"
lst = [i for i in text.split() if find_abv not in i]

print(f'Результат: {" ".join(lst)}')
