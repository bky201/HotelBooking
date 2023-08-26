from django.urls import path
from .views import (
    RoomBookingList,
    RoomList,
    RoomDetail,
    DeleteRoomBooking,
    EditBooking,
    BookingForm,
    RoomReview,
)

urlpatterns = [
    path("book/", RoomBookingList.as_view(), name="room_bookinglist"),
    path("booked/", BookingForm.as_view(), name="booking_form"),
    path("", RoomList.as_view(), name="room_list"),
    path("<int:room_id>/", RoomDetail.as_view(), name="room_detail"),
    path("review/", RoomReview.as_view(), name="room_review"),
    path("delete/<slug:pk>/", DeleteRoomBooking.as_view(), name="delete_room"),
    path("edit/<slug:pk>/", EditBooking.as_view(), name="edit_roombooking"),
]
