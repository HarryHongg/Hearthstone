from Board import *

from Magic import *



board = Board()




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
