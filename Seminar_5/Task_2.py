# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random as r

def player_vs_player():
    sweet_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nВведите имя 1 игрока: ')
    player_2 = input('\nВведите имя 2 игрока: ')

    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = r.randint(1, 2)
    if x != 1:
        print(f'{player_1} ходит первым !')
    else:
        temp = player_2
        player_2 = player_1
        player_1 = temp
        print(f'{player_1} ходит первым !')

    while sweet_total > 0:
        if count == 0:
            step = int(input(f'\nХод: {player_1} = '))
            if step > sweet_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет, попробуй еще раз: '))
            sweet_total = sweet_total - step
        if sweet_total > 0:
            print(f'\nОсталось {sweet_total}')
            count = 1
        else:
            print('Игра окончена')

        if count == 1:
            step = int(input(f'\nХод: {player_2} '))
            if step > sweet_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет, попробуй еще раз: '))
            sweet_total = sweet_total - step
        if sweet_total > 0:
            print(f'\nОсталось {sweet_total}')
            count = 0
        else:
            print('Игра окончена')

    if count == 1:
        print(f'{player_2} ПОБЕДИЛ')
    if count == 0:
        print(f'{player_1} ПОБЕДИЛ')

player_vs_player()