from Operations import *

operation = int(input(f'Введите номер операции:\n1. Добавление данных через пробел\n2. Добавление данных v2\n3. Поиск контакта\n'))

if operation == 1:
    import_data()
elif operation == 2:
    import_data2()
elif operation == 3:
    search_data()


