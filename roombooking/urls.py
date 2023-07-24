from django.urls import path
from .views import RoomBooking, RoomList, RoomDetail, DeleteRoomBooking

urlpatterns = [
    path("add/", RoomBooking.as_view(), name="book_room"),
    path("", RoomList.as_view(), name="roomlist"),
    path("<slug:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("delete/<slug:pk>/", DeleteRoomBooking.as_view(), name="delete_roombooking"),
]
