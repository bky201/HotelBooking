from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

ROOM_TITLE = (
        ('Single-bedroom', 'SINGLE-BEDROOM'),
        ('Double-bedroom', 'DOUBLE-BEDROOM'),
        ('King-room', 'KING-ROOM'),
        ('Deluxe-room', 'DELUXE-ROOM'),
        ('Twin-room', 'TWIN-ROOM'),
    )

ROOM_SERVICES = (
        ('Laundry and Dry-cleaner', 'LAUNDRY AND DRY-CLEANER'),
        ('Bath, Sauna and Swimming-pool', 'BATH, SAUNA AND SWIMMING-POOL'),
        ('Billiard, Gym and Playground', 'BILLIARD, GYM AND PLAYGROUND'),
        ('Sport-Equipment and House-appliance', 'SPORT-EQUIMENT AND HOUSE-APPLIANCE'),
        ('Car-rent, restaurant and Tour-guide', 'CAR-RENT, RESTAURANT AND TOUR-GUIDE'),
    )

FEATURES = (
        ('Balcony/terrace', 'Balcony/terrace'),
        ('Street view', 'Street view'),
        ('Garden view', 'Garden view'),
        ('Pool view', 'Pool view'),
    )
class Room(models.Model):
    """
    A model to create and manage rooms
    """
    title = models.CharField(max_length=200, choices=ROOM_TITLE, default='Single-bedroom')
    slug = models.SlugField(max_length=200, unique=True)
    number = models.IntegerField(default=1)
    features = models.CharField(max_length=30, choices=FEATURES, default='Balcony/terrace')
    beds = models.IntegerField(default=1)
    size = models.IntegerField(default=30)
    serviceOne = models.CharField(max_length=200, choices=ROOM_SERVICES, default='Laundry and Dry-cleaner')
    serviceTwo = models.CharField(max_length=200, choices=ROOM_SERVICES, default='Laundry and Dry-cleaner')
    price = models.FloatField(default=0.00)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    imageOne = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        null=True,
    )
    imageTwo = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        null=True,
    )

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.title} Room no.-{self.number}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, related_name="booking_owner", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-check_in"]

    def __str__(self):
        return f"(self.user) booked (self.room)"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='reviewed', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    comment = models.TextField(max_length=1500, null=True, blank=True)
    rating = models.PositiveIntegerField(default=5)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.title)

class About(models.Model):
    """
    A model to create and manage rooms
    """

    title = models.CharField(max_length=200, null=False, blank=False)
    content = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, 300],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

