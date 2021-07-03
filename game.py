import numpy as np

class State():
    def __init__(self, board=None, rows = 8, cols = 8):
        self.rows = rows
        self.cols = cols
        if board == None:
            self.board = np.zeros((self.rows, self.cols))
        else:
            self.board = board
        print(self.board)
        print(self.validMoves())
        pass

    def validMoves(self):
        valid_moves = []
        for i in range(self.cols):
            if self.board[0][i]==0:
                valid_moves.append(i)
        return valid_moves

    def takeAction(self, action):
        if action in self.validMoves():
            new_board = self.board
            
            pass
        else:
            print("Invalid Action")

    def findChildren(self):
        pass

if __name__=="__main__":
    game = State()