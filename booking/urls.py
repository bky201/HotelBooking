
from django.contrib import admin
from django.conf.urls import handler404, handler500, handler403
from django.urls import path, include
from django.views.generic import TemplateView
from roombooking.views import Custom404View

handler404 = Custom404View.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('roombooking/', include('roombooking.urls')),
    
]

