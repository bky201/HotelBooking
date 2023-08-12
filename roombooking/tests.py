from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Room, Booking

class TestViews(TestCase):
    """
    Test cases for booking app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "bookingads"
        password = "54321add"
        user_model = get_user_model()
        #Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create a Room
        room = Room.objects.create(title='King Room', number=10)
        # Create Booking
        booking = Booking.objects.create(
            user=self.user,
            room=room,
            check_in=datetime.now().date(),
            check_out=datetime.now().date() + timedelta(days=3)
        )