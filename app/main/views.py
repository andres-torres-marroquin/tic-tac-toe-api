from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(methods=['post'], detail=True, url_path='move')
    def move(self, request, pk=None):
        obj = self.get_object()

        if obj.winner:
            raise serializers.ValidationError(f'This game has already a winner: {obj.winner}')

        obj.move(**request.data)

        if not obj.check_winner():
            obj.computer_move()

        obj.winner = obj.check_winner()
        obj.save(update_fields=['winner'])

        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)


class GameMoveViewSet(viewsets.ModelViewSet):
    queryset = GameMove.objects.all()
    serializer_class = GameMoveSerializer
