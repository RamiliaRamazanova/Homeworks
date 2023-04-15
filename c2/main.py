from random import randint

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Клетка({self.x}, {self.y})"

# Исключения
class BoardException(Exception):
    pass

class OutOfBoardException(BoardException):
    def __str__(self):
        return "Выстрел за пределы игрового поля!"

class DoubleShootException(BoardException):
    def __str__(self):
        return "Уже стреляли в клетку с заданными координатами!"

class BoardWrongShipException(BoardException):
    pass


class Ship:
    def __init__(self, start, size, direction):
        self.start = start
        self.size = size
        self.direction = direction
        self.lives = size

    @property
    def coords(self):
        ship_cells = []
        for i in range(self.size):
            cur_x = self.start.x
            cur_y = self.start.y

            if self.direction == 0:
                cur_x += i

            elif self.direction == 1:
                cur_y += i

            ship_cells.append(Cell(cur_x, cur_y))

        return ship_cells


    def shooten(self, shot):
        return shot in self.coords


class Board:
    def __init__(self, rival = False, size = 6):
        self.size = size
        self.rival = rival

        self.count = 0

        self.field = [ ["O"]*size for _ in range(size) ]

        self.busy = []
        self.ships = []

    def __str__(self):

        board = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            board += f"\n{i+1} | " + " | ".join(row) + " |"

        if self.rival:
            board = board.replace("■", "O")
        return board

    def onBoard(self, dot):
        return ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]
        for d in ship.coords:
            for dx, dy in near:
                cur = Cell(d.x + dx, d.y + dy)
                if self.onBoard(cur) and cur not in self.busy:
                     if verb:
                         self.field[cur.x][cur.y] = "T"
                     self.busy.append(cur)


    def add_ship(self, ship):

        for d in ship.coords:
            if not self.onBoard(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.coords:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)


    def shot(self, d):
        if not self.onBoard(d):
            raise OutOfBoardException()

        if d in self.busy:
            raise DoubleShootException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.coords:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Cell(randint(0,5), randint(0, 5))
        print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Cell(x-1, y-1)
class Game:
    def __init__(self, size = 6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.rival = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size = self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Cell(randint(0, self.size), randint(0, self.size)), l, randint(0,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def print_boards(self):
        print("-"*20)
        print("Доска пользователя:")
        print(self.us.board)
        print("-"*20)
        print("Доска компьютера:")
        print(self.ai.board)
        print("-"*20)
    def loop(self):
        num = 0
        while True:
            self.print_boards()
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-"*20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-"*20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-"*20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()