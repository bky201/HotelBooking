from django.urls import path
from .views import RoomBooking, RoomList, DeleteRoom

urlpatterns = [
    path('', RoomBooking.as_view(), name='book_room'),
    path('roomlist/', RoomList.as_view(), name='roomlist'),
    path("delete/<slug:pk>/", DeleteRoom.as_view(), name='delete_room')
]