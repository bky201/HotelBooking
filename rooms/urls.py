from django.urls import path
from .views import RoomBook

urlpatterns = [
    path('', RoomBook.as_view(), name='add_room'),
]