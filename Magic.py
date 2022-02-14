class Magic:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def call(self, board):
        pass


class Defile(Magic):

    def call(self, board):
        n = 1
        body_count = 1
        while body_count > 0:
            print(f"number of defile released: {n}")
            n += 1
            board.print_board()
            for i in board.my_minions:
                i.health -= 1
            for i in board.enemies:
                i.health -= 1
            body_count = board.clean_body()
