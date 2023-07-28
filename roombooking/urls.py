from django.urls import path
from .views import RoomBookingList, RoomList, RoomDetail, DeleteRoomBooking, EditBooking, BookedRoom

urlpatterns = [
    path("book/", RoomBookingList.as_view(), name="room_bookinglist"),
    path("booked/", BookedRoom.as_view(), name="booked_room"),
    path("", RoomList.as_view(), name="room_list"),
    path("<slug:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("delete/<slug:pk>/", DeleteRoomBooking.as_view(), name="delete_roombooking"),
    path("edit/<slug:pk>/", EditBooking.as_view(), name="edit_roombooking"),
]
