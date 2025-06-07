class TicTacToe:
    def __init__(self):
        self.matrix = [[None for i in range(3)] for j in range(3)]

    def draw_board(self):
        for one_string in self.matrix:
            print(' --- --- --- ')
            board_string = "|"
            for i in one_string:
                if i is None:
                    i = " "
                board_string += " " + str(i) + " " + "|"
            print(board_string)
        print(' --- --- --- ')
        pass

    def check_diagonal(self, digit):
        result = False
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == digit: result = True
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == digit: result = True
        return result

    def transpose(self):
        result_list = [[i for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                result_list[j][i] = self.matrix[i][j]
        return result_list

    def check_column(self, checked_matrix, digit):
        result = False
        if checked_matrix[0][0] == checked_matrix[1][0] == checked_matrix[2][0] == digit: result = True
        if checked_matrix[0][1] == checked_matrix[1][1] == checked_matrix[2][1] == digit: result = True
        if checked_matrix[0][2] == checked_matrix[1][2] == checked_matrix[2][2] == digit: result = True
        return result

    def check_line(self, digit):
        new_matrix = self.transpose()
        return self.check_column(new_matrix, digit)

    def move(self, coo, digit):
        self.matrix[coo[0]][coo[1]] = digit
        self.draw_board()
        if self.check_diagonal(digit) or self.check_column(self.matrix, digit) or self.check_line(digit):
            print(str(digit) + " WON")


t = TicTacToe()
t.move((0, 1), 1)
t.move((0, 2), 0)
t.move((1, 1), 1)
t.move((1, 2), 0)
t.move((2, 1), 1)
