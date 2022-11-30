# Модуль создания файла справочника
def create_csv():
    try:
        f = open('C:/Users\Михаил/Desktop/GB\Python/Python/Seminar_7/phone.csv')
        f.close()
    except FileNotFoundError:
        file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7/phone.csv'
        with open (file, 'w', encoding='utf-8') as data:
            data.write(f'Фамилия;Имя;Организация;Номер телефона\n')
        data.close()


# модуль импорта данных 
def import_data():
    create_csv()
    file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7/phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        value = []
        value = list(input(f'Введите фамилию, имя, организацию, телефон через пробел').split())
        data.write(f'{value[0]};{value[1]};{value[2]};{value[3]}\n')
    data.close()
    print(f'Данные {value} добавлены!')


# модуль импорта данных 2
def import_data2():
    create_csv()
    file = 'C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7/phone.csv'
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
def search_data(text):
    df = pd.read_csv("C:/Users/Михаил/Desktop/GB/Python/Python/Seminar_7/phone.csv", encoding='utf-8',sep=';')
    df2 = df[df.isin(text).any(axis=1)]
    print(df2)

