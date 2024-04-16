from rest_framework import serializers

from main.models import Game, GameMove


class GameMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMove
        fields = [
            'id',
            'game',
            'board',
            'updated_at',
            'created_at',
        ]


class GameSerializer(serializers.ModelSerializer):
    moves = GameMoveSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'winner',
            'moves',
            'updated_at',
            'created_at',
        ]
