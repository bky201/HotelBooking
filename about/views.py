from django.views.generic import ListView
from roombooking.models import About


class AboutUs(ListView):
    template_name = 'about/about.html'
    model = About
    context_object_name = 'aboutpage'

    def get_queryset(self):
        return self.model.objects.all()[:4]
