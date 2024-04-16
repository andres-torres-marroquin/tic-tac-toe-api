import uuid
from django.db import models
from rest_framework import serializers
from main.decorators import autoconnect
from main.utils import check_winner


@autoconnect
class Game(models.Model):
    Players = models.TextChoices("Players", "X Y")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    winner = models.CharField(default='', choices=Players.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def post_save(self, created, *args, **kwargs):
        if created:
            board = [
                [".", ".", "."],
                [".", ".", "."],
                [".", ".", "."],
            ]
            self.moves.create(board=board)

    def most_recent_move(self):
        return self.moves.first()

    def move(self, x, y):
        game_move = self.most_recent_move()
        if game_move.board[x][y] != '.':
            raise serializers.ValidationError(f'Cannot play here (x: {x}, y: {y}) is {game_move.board[x][y]}')
        new_board = game_move.board
        new_board[x][y] = 'X'
        self.moves.create(board=new_board)

    def computer_move(self):
        from main.utils import get_random_x_y

        x, y = get_random_x_y()

        game_move = self.most_recent_move()
        if game_move.board[x][y] != '.':
            self.computer_move()
            return

        new_board = game_move.board
        new_board[x][y] = 'O'
        self.moves.create(board=new_board)

    def check_winner(self):
        board = self.most_recent_move().board
        return check_winner(board)

    @property
    def has_valid_moves(self):
        board = self.most_recent_move().board
        for row in board:
            for cell in row:
                if cell == ".":
                    return True
        return False


class GameMove(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey('Game', related_name='moves', on_delete=models.CASCADE)
    board = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
