# Создайте программу для игры в ""Крестики-нолики""

map  = [['_','_','_'],['_','_','_'],['_','_','_']]

# Вывод карты игры:
def print_map(map):
    map = str(map[0]).replace("'","").replace(",","") + '\n' \
        + str(map[1]).replace("'","").replace(",","") + '\n' \
        + str(map[2]).replace("'","").replace(",","") + '\n'
    print(map)
print_map(map)


 
# Проверка победителя:
def get_result():
    win = ""
    if (map[0][0] == map[0][1]== map[0][2] == "X") or \
        (map[1][0] == map[1][1]== map[1][2] == "X") or \
        (map[2][0] == map[2][1]== map[2][2] == "X") or \
        (map[0][0] == map[1][1]== map[2][2] == "X") or \
        (map[2][0] == map[1][1]== map[0][2] == "X") or \
        (map[0][0] == map[0][1]== map[0][2] == "X") or \
        (map[0][0] == map[1][0]== map[2][0] == "X") or \
        (map[0][1] == map[1][1]== map[2][1] == "X") or \
        (map[0][2] == map[1][2]== map[2][2] == "X"):
                win = "Победил Player_1"
    elif (map[0][0] == map[0][1]== map[0][2] == "O") or \
        (map[1][0] == map[1][1]== map[1][2] == "O") or \
        (map[2][0] == map[2][1]== map[2][2] == "O") or \
        (map[0][0] == map[1][1]== map[2][2] == "O") or \
        (map[2][0] == map[1][1]== map[0][2] == "O") or \
        (map[0][0] == map[0][1]== map[0][2] == "O") or \
        (map[0][0] == map[1][0]== map[2][0] == "O") or \
        (map[0][1] == map[1][1]== map[2][1] == "O") or \
        (map[0][2] == map[1][2]== map[2][2] == "O"):
            win = "Победил Player_2"   
    return win
count = 0
game_over = False
Player1 = True

while game_over == False:

    if Player1 == True and count == 0:
        symbol = "X"
        step = (input(f'Player_1 введите координаты\n').split(" "))
        
        if (0<=int(step[0])<=2 or 0<=int(step[1])<=2):

            if map[int(step[0])][int(step[1])] == "_" :
                map[int(step[0])][int(step[1])] = symbol
                count = 1
                print_map(map)
            else:
                print("Данный ход не допустим")

    elif count == 1:
        symbol = "O"
        step = (input(f'Player_2 введите координаты\n').split(" "))
        
        if (0<=int(step[0])<=2 or 0<=int(step[1])<=2):
            
            if map[int(step[0])][int(step[1])] == "_" :
                map[int(step[0])][int(step[1])] = symbol
                count = 0
                print_map(map)
            else:
                print("Данный ход не допустим")
        
    if step != "":
        win = get_result() 
        if win != "":
            game_over = True
        else:
            game_over = False
        print(win)
    else:
        print("Ничья!")
        game_over = True
    Player1 = not(Player1) 
 
