from django import forms
# from djrichtextfield.widgets import RichTextWidget
from .models import Room

class BookForm(forms.ModelForm):
    """ Form to create a booking """
    class Meta:
        model = Room
        fields = ['title', 'size', 'features', 'available_on']

        labels = {
            'title': 'Room Title',
            'size': 'Room Size',
            'features': 'Room Features',
            'available_on': 'Room available'
        }