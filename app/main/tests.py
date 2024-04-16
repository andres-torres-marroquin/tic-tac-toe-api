from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.utils import check_winner
from main.models import Game


class TicTacToeTests(TestCase):
    def test_horizontal_win(self):
        board = [
            ["X", "X", "X"],
            [".", ".", "."],
            [".", ".", "."],
        ]
        self.assertEqual(check_winner(board), "X")

        board = [
            [".", ".", "."],
            ["O", "O", "O"],
            [".", ".", "."],
        ]
        self.assertEqual(check_winner(board), "O")

    def test_vertical_win(self):
        board = [
            ["X", ".", "."],
            ["X", ".", "."],
            ["X", ".", "."],
        ]
        self.assertEqual(check_winner(board), "X")

        board = [
            [".", "O", "."],
            [".", "O", "."],
            [".", "O", "."],
        ]
        self.assertEqual(check_winner(board), "O")

    def test_diagonal_win(self):
        board = [
            ["X", ".", "."],
            [".", "X", "."],
            [".", ".", "X"],
        ]
        self.assertEqual(check_winner(board), "X")

        board = [
            [".", ".", "O"],
            [".", "O", "."],
            ["O", ".", "."],
        ]
        self.assertEqual(check_winner(board), "O")

    def test_no_winner(self):
        board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ]
        self.assertEqual(check_winner(board), "")

        board = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
        ]
        self.assertEqual(check_winner(board), "")

    def test_full_board_no_winner(self):
        board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
        self.assertEqual(check_winner(board), "")


class GameTests(APITestCase):
    def test_create_a_game(self):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

    @patch('main.utils.get_random_x_y')
    def test_move_a(self, get_random_x_y_mock):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

        data = {"x": 1, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 0, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 3)

        data = {"x": 0, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 0, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 5)

        data = {"x": 2, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], 'X')
        self.assertEqual(len(data['moves']), 6)

    @patch('main.utils.get_random_x_y')
    def test_move_b(self, get_random_x_y_mock):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

        data = {"x": 0, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 3)

        data = {"x": 0, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 5)

        data = {"x": 0, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], 'X')
        self.assertEqual(len(data['moves']), 6)

    @patch('main.utils.get_random_x_y')
    def test_move_c(self, get_random_x_y_mock):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

        data = {"x": 0, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 3)

        data = {"x": 0, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 5)

        data = {"x": 2, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], 'O')
        self.assertEqual(len(data['moves']), 7)

    @patch('main.utils.get_random_x_y')
    def test_move_d(self, get_random_x_y_mock):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

        data = {"x": 0, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 0, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 3)

        data = {"x": 0, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 5)

        data = {"x": 1, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 7)

        data = {"x": 2, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 2, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 9)

        data = {"x": 2, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 2, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], 'X')
        self.assertEqual(len(data['moves']), 10)

    @patch('main.utils.get_random_x_y')
    def test_move_e(self, get_random_x_y_mock):
        url = reverse('game-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 1)

        data = {"x": 0, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 0, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 3)

        data = {"x": 0, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 5)

        data = {"x": 1, "y": 2}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 1, 1
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 7)

        data = {"x": 2, "y": 0}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 2, 2
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 9)

        data = {"x": 2, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        get_random_x_y_mock.return_value = 2, 0
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data['winner'], '')
        self.assertEqual(len(data['moves']), 10)

        data = {"x": 2, "y": 1}
        url = reverse('game-move', args=[response.data['id']])
        response = self.client.post(url, data, format='json')
        data = response.data
        self.assertEqual(data[0], 'Cannot play here (x: 2, y: 1) is X')
