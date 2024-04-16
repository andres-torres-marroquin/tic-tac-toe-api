

from django.urls import path, include
from rest_framework import routers
from main.views import GameMoveViewSet
from main.views import GameViewSet


router = routers.DefaultRouter()
router.register(r'games', GameViewSet, basename='games')
router.register(r'game-moves', GameMoveViewSet, basename='game-moves')


urlpatterns = [
    path('api/', include(router.urls)),
]
