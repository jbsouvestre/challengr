'''
Created on Feb 13, 2015

@author: utku
'''
import json


class CheckersBoard(object):

    def __init__(self, serialized_board, turn):
        pass

    def move(self, move):
        return True

    def is_game_over(self):
        return False

    def get_winner(self):
        return None | "white" | "black"

    def serialize(self):
        return json.dumps({})
