from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect
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
    
    
class BookingForm(LoginRequiredMixin, CreateView):
    """Create booking"""

    form_class = BookForm
    template_name = "roombooking/booking_form.html"
    model = Booking
    success_url = "/roombooking/"
    context_object_name = "bookform"

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        # Check room availability using the check_room_availability method
        if not self.check_room_availability(room, check_in, check_out):
            # Room is not available, show an error message
            messages.error(self.request, "Booking is not possible at the given date.")
            return self.form_invalid(form)

        return super().form_valid(form)

    def check_room_availability(self, room, check_in, check_out):
        existing_bookings = Booking.objects.filter(room=room, check_in__lt=check_out, check_out__gt=check_in)

        for booking in existing_bookings:
            if booking.user == self.request.user:
                # The same user has already booked the room for the specified dates
                return False

        return True


        
class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a booking"""
    template_name = "roombooking/edit_booking.html"
    model = Booking
    form_class = BookForm
    success_url = reverse_lazy("room_bookinglist")

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRoomBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a room booking"""

    model = Booking
    success_url = reverse_lazy("room_bookinglist")

    def test_func(self):
        return self.request.user == self.get_object().user
