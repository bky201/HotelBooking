from django import forms

# from djrichtextfield.widgets import RichTextWidget
from .models import Booking


class BookForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = ["user", "room", 'check_in', 'check_out']

        labels = {
            "user": "Room user",
            "room": "Room title",
            "check_in": "Booking start date",
            "check_out": "Booking end date",
        }
