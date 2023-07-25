from django.urls import path
from .views import AboutUs


urlpatterns = [
    path('', AboutUs.as_view(), name='aboutpage')
]