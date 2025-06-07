def draw_board(board):
    for one_string in board:
        print(' --- --- --- ')
        board_string = "|"
        for i in one_string:
            if i == None:
                i = " "
            board_string+= " " + str(i) + " " + "|"
        print(board_string)
    print(' --- --- --- ')
    pass

# draw_board([
#     [None, 0, 1],
#     [None, None, None],
#     [1, 0, 1]
# ])

# [
#     [None, 0,    1],
#     [None, None, None],
#     [1,    0,    1]
# ]


#  --- --- ---
# |   | 0 | 1 |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# | 1 | 0 | 1 |
#  --- --- ---
