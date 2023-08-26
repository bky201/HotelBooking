from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {"profile": profile,}

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user