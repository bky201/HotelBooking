from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Room
from .forms import BookForm

class RoomBook(LoginRequiredMixin, CreateView):
    model = Room
    form_class = BookForm
    queryset = Room.objects.filter(status=1).order_by('-available_on')
    template_name = 'rooms/add_room.html'
    success_url = "/rooms/"
    paginate = 6

    def book_valid(self, form):
        form.instance.user = self.request.user
        return super(RoomBook, self).book_valid(form)