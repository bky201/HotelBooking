from django.urls import path
from .views import RoomBooking, RoomList, RoomDetail, DeleteRoom

urlpatterns = [
    path("", RoomBooking.as_view(), name="book_room"),
    path("roomlist/", RoomList.as_view(), name="roomlist"),
    path("<slug:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("delete/<slug:pk>/", DeleteRoom.as_view(), name="delete_room"),
]
