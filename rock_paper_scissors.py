import random






def how_much_win():  # Функция выбора до скольки побед идет игра
    win = ''
    while win == '':
        try:
            win = int(input('До скольки побед играем?'))
            if win == 1:
                print(f'Игра идет до {win} победы')
            else:
                print(f'Игра идет до {win} побед')
        except:
            print('Неверно указано значение')
            win == ' '
    return win


def player_element():  # Функция выбора игрока
    player_element1 = ''
    while player_element1 not in element[1:]:
        try:
            player_element1 = element[int(
                input('Выберите:\n 1)камень\n 2)ножницы\n 3)бумага\n'))]
            if player_element1 == element[0]:
                print('Неверно указано значение')
                player_element1 = ''
        except:
            print('Неверно указано значение')
            player_element1 = ''
    return player_element1


def how_win():															#Показывает счет побед
	print(f'Счет:\nИгрок {win_player}\nКомпьютер {win_comp}\n')



win_player = 0 															# Переменные счетчики
win_comp = 0
win = how_much_win()
element = [' ', 'камень', 'ножницы', 'бумага']


while win_player != win and win_comp != win:							# алгоритм игры

    player = player_element()
    comp = element[random.randint(1, 3)]

    print(f'Игрок: {player}')
    print(f'Компьютер: {comp}\n')

    if player == 'камень' and comp == 'ножницы':
        win_player += 1
        player_element1 = ''
        how_win()
    elif player == 'бумага' and comp == 'камень':
        win_player += 1
        player_element1 = ''
        how_win()
    elif player == 'ножницы' and comp == 'бумага':
        win_player += 1
        player_element1 = ''
        how_win()
    elif player == comp:
        print('ничья\n')
        how_win()
        player_element1 = ''
    else:
        win_comp += 1
        player_element1 = ''
        how_win()

if win_player > win_comp:  												# Вывод победителя
    print('Вы выиграли!:)')
else:
    print('Вы проиграли:(')
