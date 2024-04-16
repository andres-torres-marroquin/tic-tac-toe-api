import uuid
import random
from django.db import models
from rest_framework import serializers
from main.decorators import autoconnect


@autoconnect
class Game(models.Model):
    Players = models.TextChoices("Players", "X Y")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    winner = models.CharField(default='', choices=Players.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        game_move = self.most_recent_move()
        if game_move.board[x][y] != '.':
            self.computer_move()
            return

        new_board = game_move.board
        new_board[x][y] = 'O'
        self.moves.create(board=new_board)

    def check_winner(self):
        board = self.most_recent_move().board

        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ".":
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ".":
                return board[0][col]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
            return board[0][2]

        # No winner
        return None


class GameMove(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey('Game', related_name='moves', on_delete=models.CASCADE)
    board = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


