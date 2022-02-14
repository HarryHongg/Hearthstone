import random

from Board import *
from Minion import *
from Magic import *

num_my_minion = random.randrange(3, 7)
num_enemies = random.randrange(num_my_minion, 7)
my_minions = []
enemies = []
for i in range(num_my_minion):
    my_minions.append(Minion(chr(random.randint(65, 122)), random.randint(1, 8), random.randint(1, 9)))
for i in range(num_enemies):
    enemies.append(Minion(chr(random.randint(65, 122)), random.randint(1, 8), random.randint(1, 9)))

board = Board(my_minions, enemies)




print("beginning board")
board.print_board()
board.defile_data(True)
action_list = board.prepare()
print(action_list)
print()
print("board after prepare")
board.print_board()
board.defile_data(True)
defile = Defile("defile", 3)
defile.call(board)
board.print_board()
