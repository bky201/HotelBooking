
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('roombooking/', include('roombooking.urls')),
    
]

