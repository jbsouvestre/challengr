'''
Created on Jan 16, 2013

@author: utku
'''

from django.conf import settings

import celery
from apps.game.models import Game


@celery.task
def make_program_move(game, program):
    if game.turn == Game.WHITE:
        assert game.white == program
    if game.turn == Game.BLACK:
        assert game.black == program
