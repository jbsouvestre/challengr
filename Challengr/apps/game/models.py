from django.db import models
from apps.player.models import Player
from apps.game.exceptions import InvalidMove
import json
from apps.checkers.commands import CheckersBoard
from django.utils import timezone

# Create your models here.


class Game(models.Model):
    WHITE = "white"
    BLACK = "black"
    TURN = ((WHITE, WHITE), (BLACK, BLACK))

    PENDING = "pending"
    STARTED = "started"
    OVER = "over"
    STATE = ((PENDING, PENDING), (STARTED, STARTED), (OVER, OVER))

    CHECKERS = "checkers"
    GAME_TYPE = ((CHECKERS, CHECKERS),)

    white = models.ForeignKey(Player, related_name="white_player")
    black = models.ForeignKey(Player, related_name="black_player")
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)

    game_type = models.CharField(choices=GAME_TYPE, max_length=10)

    move = models.PositiveIntegerField(default=0)
    turn = models.CharField(choices=TURN, max_length=10, default=WHITE)
    state = models.CharField(choices=STATE, max_length=10, default=PENDING)

    winner = models.CharField(choices=TURN, max_length=10, default=None, null=True)

    board = models.TextField()
    history = models.TextField(default="[]")

    def end_turn(self):
        if self.turn == Game.WHITE:
            self.turn = Game.BLACK
        else:
            self.turn = Game.WHITE

        self.move += 1

    def make_move(self, turn, move):
        assert self.state != Game.OVER
        if self.state == Game.PENDING:
            self.state = Game.STARTED

        board = CheckersBoard(self.board, turn)
        if not board.move(move):
            raise InvalidMove()

        self.board = board.serialize()

        try:
            current_history = json.loads(self.history)
        except ValueError:
            current_history = []

        self.history = json.dumps(current_history)
        self.end_turn()

        if board.is_game_over():
            self.state = Game.OVER
            self.ended_at = timezone.now()
            self.winner = board.get_winner()
