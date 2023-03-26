def intro():
    print('          Крестики-нолики')
    print('Для хода введите координаты в формате "x y",')
    print('где x - номер строки, y - номер столбца')
    print()


def board():
    print('  0 1 2')
    for i, row in enumerate(positions):
        row_info = f"{i} {' '.join(row)} "
        print(row_info)


def coords_type():
    while True:
        coords = input('Введите координаты').split()

        if len(coords) != 2:
            print('Ошибка! Нужно ввести 2 координаты')
            continue

        x, y = coords

        if x.isdigit() or y.isdigit():
            x, y = int(x), int(y)
        else:
            print('Ошибка! Нужно ввести 2 числа')
            continue

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Ошибка! Можно вводить только числа от 0 до 2')
            continue

        if positions[x][y] != " ":
            print('Ошбика! Позиция уже сыграна')
            continue

        return x, y


def check_win():
    win_cord = (
                ((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(positions[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


positions = [[" "] * 3 for i in range(3)]

intro()
count = 0
while True:
    count += 1
    board()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = coords_type()
    if count % 2 == 1:
        positions[x][y] = "X"
    else:
        positions[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break

