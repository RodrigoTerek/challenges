class TicTacToe(object):
    def __init__(self, n):
        self.matrix = []
        self.playerChars = ['_', 'X', 'O']

        for _ in range(n):
            arr = []
            for _ in range(n):
                arr.append('_')
            self.matrix.append(arr)

    def move(self, row, col, player):
        if self.matrix[row][col] != '_':
            print('Invalid place')
            return

        self.matrix[row][col] = self.playerChars[player]

        self.draw()

        return self.checkWinner()

    def checkWinner(self):
        rowFlag = True
        colFlag = True
        diagFlag = True
        diagFlag2 = True

        diagChar = self.matrix[0][0]
        diagChar2 = self.matrix[0][- 1]

        for i, _ in enumerate(self.matrix):
            rowChar = self.matrix[i][0]
            colChar = self.matrix[0][i]

            for j, _ in enumerate(self.matrix):
                if self.matrix[i][j] != rowChar:
                    rowFlag = False

                if self.matrix[j][i] != colChar:
                    colFlag = False

            if rowFlag:
                print('Winner is ' + rowChar)
                return

            if colFlag:
                print('Winner is ' + colChar)
                return

            if self.matrix[i][i] != diagChar:
                diagFlag = False

            if self.matrix[i][i] != diagChar2:
                diagFlag2 = False

        if diagFlag:
            print('Winner is ' + diagChar)
            return

        if diagFlag2:
            print('Winner is ' + diagChar2)
            return

        return self.draw()

    def draw(self):
        for row in self.matrix:
            print(row)
        print('---------------')


print('---------------')
board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
