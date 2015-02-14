'''
Created on Feb 13, 2015

@author: utku
'''


class GameException(Exception):
    pass


class InvalidMove(GameException):

    def __init__(self, board, turn, move):
        self.board = board
        self.turn = turn
        self.move = move
        super(InvalidMove, self).__init__()
