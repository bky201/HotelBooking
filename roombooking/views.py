from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.db.models import Q

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from .models import Room, Booking
from .forms import BookForm


class RoomList(ListView):
    """View all rooms"""

    template_name = "roombooking/room_list.html"
    model = Room
    context_object_name = "roomlist"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            roomlist = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            roomlist = self.model.objects.all()
        return roomlist
    

class RoomDetail(DetailView):
    """View a single room"""

    template_name = "roombooking/room_detail.html"
    model = Room
    context_object_name = "roomdetail"

class RoomBookingList(LoginRequiredMixin, ListView):
    """View all booking"""

    template_name = "roombooking/room_booking.html"
    model = Booking
    queryset = Booking.objects.all().order_by("-check_in")
    context_object_name = "roombook"

    def get_queryset(self):
        return self.model.objects.all()
    
    
class BookedRoom(LoginRequiredMixin, CreateView):
    """Create booking"""

    form_class = BookForm
    template_name = "roombooking/booking_list.html"
    model = Booking
    success_url = "/roombooking/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def check_room_availability(self, room, check_in, check_out):
        check_list = []
        queryset = self.model.objects.filter(room=room)
        for booking in queryset:
            if booking.check_in > check_out or booking.check_out < check_in:
                check_list.append(True)
            else:
                check_list.append(False)
        return all(check_list)
    


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a booking"""
    template_name = "roombooking/edit_booking.html"
    model = Room
    form_class = BookForm
    success_url = "/roombooking/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRoomBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a room booking"""

    model = Room
    success_url = "/roombooking/"

    def test_func(self):
        return self.request.user == self.get_object().user
