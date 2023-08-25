from django import forms

# from djrichtextfield.widgets import RichTextWidget
from .models import Booking, Review


class BookForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = ["user", "room", "ch_in", "ch_out"]

        labels = {
            "user": "Room user",
            "room": "Room title",
            "ch_in": "Booking start date",
            "ch_out": "Booking end date",
        }


class ReviewForm(forms.ModelForm):
    """Form to create a review"""

    class Meta:
        model = Review
        fields = ["rating", "title", "comment"]

        labels = {
            "rating": "User star rating",
            "title": "Review title",
            "comment": "User review",
        }
