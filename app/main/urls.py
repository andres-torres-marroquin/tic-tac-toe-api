from django.urls import path, include
from rest_framework import routers
from main.views import GameMoveViewSet
from main.views import GameViewSet


router = routers.DefaultRouter()
router.register(r'games', GameViewSet, basename='game')
router.register(r'game-moves', GameMoveViewSet, basename='game-move')


urlpatterns = [
    path('api/', include(router.urls)),
]
