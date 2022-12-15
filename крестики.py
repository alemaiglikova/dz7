maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def play():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])
    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])
    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def steps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win
game_over = False
player1 = True

while game_over == False:
    play()
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок2, ваш ход: "))

    steps(step, symbol)  # делаем ход в указанную ячейку
    win =result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

play()
print("Победил", win)


