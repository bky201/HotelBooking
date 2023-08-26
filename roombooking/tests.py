from datetime import datetime, timedelta
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Room, Booking


class TestViews(TestCase):
    """
    Test cases for booking app as logged in user
    """

    def setUp(self):
        """Setup test"""
        username = "bookadmin"
        password = "Add12345"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username, password=password, is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create a Room
        self.image_path = "static/images/img4.webp"
        self.imagOne_path = "static/images/img1.webp"
        self.imagTwo_path = "static/images/img2.webp"
        room = Room.objects.create(
            title="Single-bedroom",
            image=self.image_path,
            imageOne=self.imagOne_path,
            imageTwo=self.imagTwo_path,
            number=10,
        )
        aware_ch_in = timezone.localtime()
        aware_ch_out = aware_ch_in + timedelta(days=1)

        # Create Booking
        booking = Booking.objects.create(
            user=self.user, room=room, ch_in=aware_ch_in, ch_out=aware_ch_out
        )

    def test_room_list(self):
        """Test Room List"""
        response = self.client.get("/roombooking/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_list.html")

    def test_booking_list(self):
        """Test Manage Booking"""
        response = self.client.get("/roombooking/book/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_booking.html")

    def test_room_reviews_list(self):
        """Test Room Reviews List"""
        response = self.client.get("/roombooking/review/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_reviews.html")

    def test_booking_detail_page(self):
        "Test Room Details"
        response = self.client.get("/roombooking/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_detail.html")

    def test_edit_booking_page(self):
        "Test edit booking for superuser"
        response = self.client.get("/roombooking/edit/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/edit_booking.html")

    def test_make_booking_page(self):
        "Test create booking for superuser"
        response = self.client.get("/roombooking/booked/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/booking_form.html")

    def test_delete_unauthorized(self):
        """
        Test logged in user cannot delete
        other user booking
        """
        user_model = get_user_model()
        # Create new user for testing 403 errors
        username = "newuser"
        password = "newpass1"
        user = user_model.objects.create_user(
            username=username, password=password, is_superuser=False
        )
        logged_in = self.client.login(username=username, password=password)

        # Try to delete the booking created by bookadmin
        booking_id = 1
        url = reverse("delete_room", args=[booking_id])
        self.assertTrue(logged_in)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_edit_unauthorized(self):
        """
        Test logged in user cannot edit
        other user booking
        """
        user_model = get_user_model()
        # Create new user for testing 403 errors
        username = "newuser"
        password = "newpass1"
        user = user_model.objects.create_user(
            username=username, password=password, is_superuser=False
        )
        logged_in = self.client.login(username=username, password=password)

        # Try to edit the booking created by bookadmin
        booking_id = 1
        url = reverse("edit_roombooking", args=[booking_id])
        self.assertTrue(logged_in)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """Test views when user is not logged in"""

    def test_manage_booking_auth_redirect(self):
        """Test redirect on manage booking page"""
        response = self.client.get("/roombooking/book/")
        self.assertEqual(response.status_code, 302)

    def test_create_booking_auth_redirect(self):
        """Test redirect on make booking page"""
        response = self.client.get("/roombooking/booked/")
        self.assertEqual(response.status_code, 302)

    def test_delete_booking(self):
        """Test redirect on delete booking"""
        response = self.client.get("/roombooking/delete/1/")
        self.assertEqual(response.status_code, 302)

    def test_edit_booking(self):
        """Test redirect on edit booking page"""
        response = self.client.get("/roombooking/edit/1/")
        self.assertEqual(response.status_code, 302)


class TestUnsecuredViews(TestCase):
    def setUp(self):
        """Setup test"""
        # Create a Room
        self.image_path = "static/images/img4.webp"
        self.imagOne_path = "static/images/img1.webp"
        self.imagTwo_path = "static/images/img2.webp"
        room = Room.objects.create(
            title="Single-bedroom",
            image=self.image_path,
            imageOne=self.imagOne_path,
            imageTwo=self.imagTwo_path,
            number=10,
        )

    """ Test views no auth required """

    def test_room_view(self):
        """Test rooms view"""
        response = self.client.get("/roombooking/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_list.html")

    def test_room_detail_page(self):
        """Test room detail page renders correct page"""
        response = self.client.get("/roombooking/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roombooking/room_detail.html")
