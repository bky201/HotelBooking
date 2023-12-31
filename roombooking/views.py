from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.db.models import Q
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone


from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from .models import Room, Booking, Review
from .forms import BookForm, ReviewForm
from django.db.models import Q
from django.db.models import Avg


class RoomList(ListView):
    """View all rooms"""

    template_name = "roombooking/room_list.html"
    model = Room
    context_object_name = "roomlist"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            query = self.request.GET.get("q")
        if query:
            roomlist = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(features__icontains=query)
                | Q(serviceOne__icontains=query)
                | Q(serviceTwo__icontains=query)
            )
        else:
            roomlist = self.model.objects.all()

        return roomlist


class RoomDetail(View):
    """View a single room"""

    def get(self, request, room_id, *args, **kwargs):
        queryset = Room.objects.all()
        room = get_object_or_404(queryset, id=room_id)
        reviews = Review.objects.filter(room_id=room_id).order_by("created_on")

        user_booked = Booking.objects.filter(
            user=request.user.id, room_id=room_id
        ).exists()

        return render(
            request,
            "roombooking/room_detail.html",
            {
                "room": room,
                "reviews": reviews,
                "user_booked": user_booked,
            },
        )

    def post(self, request, room_id, *args, **kwargs):
        queryset = Room.objects.all()
        room = get_object_or_404(queryset, id=room_id)
        reviews = Review.objects.filter(room_id=room_id).order_by("created_on")

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            rating = review_form.cleaned_data["rating"]
            title = review_form.cleaned_data["title"]
            comment = review_form.cleaned_data["comment"]

            # Check if the user's review exists
            review_exist, created = Review.objects.get_or_create(
                user=request.user, room=room
            )

            if not created:
                review_exist.rating = int(rating)
                review_exist.title = title
                review_exist.comment = comment
                review_exist.save()
                messages.success(
                    request,
                    "Review for room updated successfully."
                        )
            else:
                # If the review was just created, set its attributes
                review_exist.rating = int(rating)
                review_exist.title = title
                review_exist.comment = comment
                review_exist.save()
                messages.success(
                    request,
                    "Review for room created successfully."
                    )

            # Redirect to the room detail page after submitting the review
            return redirect("room_detail", room_id=room_id)

        return render(
            request,
            "roombooking/room_detail.html",
            {
                "room": room,
                "reviews": reviews,
                "review_form": review_form,
                "user_booked": Booking.objects.filter(
                    user=request.user.id, room_id=room_id
                ).exists(),
            },
        )


class RoomReview(View):
    """View a single room"""

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all().order_by("created_on")

        return render(
            request,
            "roombooking/room_reviews.html",
            {
                "reviews": reviews,
            },
        )


class RoomBookingList(LoginRequiredMixin, ListView):
    """View all booking"""

    template_name = "roombooking/room_booking.html"
    model = Booking
    context_object_name = "roombook"

    def get_queryset(self):
        # Modify the queryset to order it by ch_in in descending order
        return self.model.objects.all().order_by("-ch_in")


class RoomAvailabilityMixin:
    def check_room_availability(
        self, room, ch_in, ch_out, current_booking=None
            ):
        # Check if ch_in is greater than or equal to the current date
        if ch_in < timezone.now().date():
            messages.error(
                self.request,
                "check_in date is not valid please enter a valid date."
            )
            return False

        # Check if ch_out is greater than or equal to ch_in
        if ch_out <= ch_in:
            messages.error(
                self.request,
                "check_out date is not valid please enter a valid date."
            )
            return False

        # Create a queryset for existing bookings
        # that overlap with the given dates
        existing_bookings = Booking.objects.filter(
            room=room, ch_in__lt=ch_out, ch_out__gt=ch_in
        )

        # Exclude the current booking if provided
        if current_booking:
            existing_bookings = existing_bookings.exclude(
                pk=current_booking.pk
                )

        for booking in existing_bookings:
            # Check if there's an overlap in date ranges
            if booking.ch_in < ch_out and booking.ch_out > ch_in:
                # There's an overlap in bookings
                messages.error(
                    self.request,
                    "Booking date is already reserved try different date."
                )
                return False

        # If no overlapping bookings were found
        # and conditions are met, the room is available
        return True


class BookingForm(
    LoginRequiredMixin, UserPassesTestMixin, RoomAvailabilityMixin, CreateView
        ):
    """Create booking"""

    form_class = BookForm
    template_name = "roombooking/booking_form.html"
    model = Booking
    success_url = reverse_lazy("room_bookinglist")
    context_object_name = "bookform"

    def test_func(self):
        # Implement your custom permission logic here
        # Return True if the user has permission, False otherwise
        return self.request.user.is_authenticated

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data["room"]
        ch_in = form.cleaned_data["ch_in"]
        ch_out = form.cleaned_data["ch_out"]

        # Check room availability using the check_room_availability method
        if not self.check_room_availability(room, ch_in, ch_out):
            return self.form_invalid(form)
        messages.success(self.request, f"Booking {room} Completed Successful")

        return super().form_valid(form)


class EditBooking(
    LoginRequiredMixin, UserPassesTestMixin, RoomAvailabilityMixin, UpdateView
):
    """Edit a booking"""

    template_name = "roombooking/edit_booking.html"
    model = Booking
    form_class = BookForm
    success_url = reverse_lazy("room_bookinglist")

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data["room"]
        ch_in = form.cleaned_data["ch_in"]
        ch_out = form.cleaned_data["ch_out"]

        # Check room availability using the check_room_availability method
        if not self.check_room_availability(
            room, ch_in, ch_out, current_booking=self.object
        ):
            return self.form_invalid(form)

        messages.success(self.request, f"Booking Updated {room} Successful")

        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRoomBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a room booking"""

    model = Booking
    success_url = reverse_lazy("room_bookinglist")

    def form_valid(self, form):
        """Display message on delete success"""
        messages.success(self.request, "Successfully deleted booking")
        return super(DeleteRoomBooking, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
