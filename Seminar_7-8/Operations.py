# Модуль создания файла справочника
def create_csv():
    try:
        f = open('C:/Users\Михаил/Desktop/GB\Python/Python/Seminar_7-8/phone.csv')
        f.close()
    except FileNotFoundError:
        file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7-8/phone.csv'
        with open (file, 'w', encoding='utf-8') as data:
            data.write(f'Фамилия;Имя;Организация;Номер телефона\n')
        data.close()


# модуль импорта данных 
def import_data():
    create_csv()
    file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7-8/phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        value = []
        value = list(input(f'Введите фамилию, имя, организацию, телефон через пробел').split())
        data.write(f'{value[0]};{value[1]};{value[2]};{value[3]}\n')
    data.close()
    print(f'Данные {value} добавлены!')


# модуль импорта данных 2
def import_data2():
    create_csv()
    file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7-8/phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        value = []
        value.append(input(f'Введите фамилию: '))
        value.append(input(f'Введите имя: '))
        value.append(input(f'Введите организацию: '))
        value.append(input(f'Введите номер телефона: '))
        data.write(f'{value[0]};{value[1]};{value[2]};{value[3]}\n')
    data.close()
    print(f'Данные {value} добавлены!')
        

# Поиск контакта
import pandas as pd
import numpy as np
def search_data():
    text = set(list(input("Введите данные для поиска: ").split()))
    df = pd.read_csv("C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7-8/phone.csv", encoding='utf-8',sep=';')
    df2 = df[df.isin(text).any(axis=1)]
    print(df2)



# Поиск контакта 2
def search_data2():
    text = (input("Введите данные для поиска: "))
    with open("C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7-8/phone.csv", 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            if ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
        t = []
        if len(data) > 0:
            for item in data:
                if text in item:
                    t = item
                elif t==[]:
                    t = None
        elif t==[]:
            t = None
        if t != None:
                    print(f'Фамилия:  {t[0]}\nИмя: {t[1]}\nОрганизация: {t[2]}\nТелефон: {t[3]}')
        else:
            print("Данные не обнаружены")

