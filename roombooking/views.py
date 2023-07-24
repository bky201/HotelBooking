from django.views.generic import CreateView, ListView, DetailView, DeleteView

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Room
from .forms import BookForm


class RoomList(ListView):
    """View all rooms"""

    template_name = "roombooking/room_list.html"
    model = Room
    context_object_name = "roomlist"
    paginate_by = 6


class RoomDetail(DetailView):
    """View a single room"""

    template_name = "roombooking/room_detail.html"
    model = Room
    context_object_name = "roomdetail"


class RoomBooking(LoginRequiredMixin, CreateView):
    """Create booking"""

    template_name = "roombooking/book_room.html"
    model = Room
    queryset = Room.objects.filter(status=1).order_by("-available_on")
    form_class = BookForm
    success_url = "/roombooking/"

    def book_valid(self, form):
        form.instance.user = self.request.user
        return super(RoomBooking, self).book_valid(form)


class DeleteRoomBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a room booking"""

    model = Room
    success_url = "/roombooking/"

    def test_func(self):
        return self.request.user == self.get_object().user
