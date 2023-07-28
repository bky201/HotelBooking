from django.views.generic import ListView
from roombooking.models import Room


class Index(ListView):
    template_name = 'home/index.html'
    model = Room
    context_object_name = 'roomlist'

    def get_queryset(self):
        return self.model.objects.all()[:3]
