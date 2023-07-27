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
    paginate_by = 6

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


class RoomBooking(LoginRequiredMixin, CreateView):
    """Create booking"""

    template_name = "roombooking/room_booking.html"
    model = Booking
    queryset = Room.objects.filter(status=1).order_by("-number")
    form_class = BookForm
    success_url = "/roombooking/"

    def book_valid(self, form):
        form.instance.user = self.request.user
        return super(RoomBooking, self).book_valid(form)


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
