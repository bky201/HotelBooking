from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

STATUS = ((1, "Available"), (0, "Not availab"))

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
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    status = models.IntegerField(choices=STATUS)
    rating = models.ManyToManyField(User, related_name="room_rate", blank=True)

    class Meta:
        ordering = ["-number"]

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-check_in"]

    def __str__(self):
        return f"(self.user) booked (self.room)"


class Comment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    

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
