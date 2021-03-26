import numpy as np

class state:
    def __init__(self, board=None):
        if board == None:
            self.board == np.zeros()
        self.board = board