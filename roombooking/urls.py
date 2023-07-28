from django.urls import path
from .views import RoomBooking, RoomList, RoomDetail, DeleteRoomBooking, EditBooking

urlpatterns = [
    path("", RoomBooking.as_view(), name="room_booking"),
    path("", RoomList.as_view(), name="roomlist"),
    path("<slug:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("delete/<slug:pk>/", DeleteRoomBooking.as_view(), name="delete_roombooking"),
    path("edit/<slug:pk>/", EditBooking.as_view(), name="edit_roombooking"),
]
