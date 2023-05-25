
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
                self.field[cur.x][cur.y] = '+'
                # if self.onBoard(cur) and cur not in self.busy:
                #     if verb:
                #         self.field[cur.x][cur.y] = "."
                #     self.busy.append(cur)

b = Board()
b.contour(Ship(Cell(2,1), 3, 1))
print(b)