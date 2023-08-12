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
            is_superuser=True,
            is_staff=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)