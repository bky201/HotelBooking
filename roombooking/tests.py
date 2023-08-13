from datetime import datetime, timedelta
from django.utils import timezone
from django.test import TestCase, client
from django.contrib.auth import get_user_model
from .models import Room, Booking

class TestViews(TestCase):
    """
    Test cases for booking app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "bookadmin"
        password = "Add12345"
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
        self.image_path = 'static/images/img4.jpg'
        self.imagOne_path = 'static/images/img1.jpg'
        self.imagTwo_path = 'static/images/img2.jpg'
        room = Room.objects.create(
            title='Single-bedroom', 
            image=self.image_path,
            imageOne = self.imagOne_path,
            imageTwo = self.imagTwo_path, 
            number=10)
        aware_check_in = timezone.localtime()
        aware_check_out = aware_check_in + timedelta(days=1)

        # Create Booking
        booking = Booking.objects.create(
            user=self.user,
            room=room,
            check_in=aware_check_in,
            check_out=aware_check_out 
        )

    def test_room_list(self):
        """ Test Room List """
        response=self.client.get('/roombooking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombooking/room_list.html')

    def test_booking_list(self):
        """ Test Manage Booking """
        response = self.client.get('/roombooking/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombooking/room_booking.html')

    def test_booking_detail_page(self):
        " Test Room Details "
        response = self.client.get('/roombooking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombooking/room_detail.html')

    def test_edit_booking_page(self):
        " Test edit booking for superuser"
        response = self.client.get('/roombooking/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombooking/edit_booking.html')
        
    def test_make_booking_page(self):
        " Test create booking for superuser"
        response = self.client.get('/roombooking/booked/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roombooking/booking_form.html')

    
