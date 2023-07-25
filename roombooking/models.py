from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

STATUS = ((0, "Available"), (1, "Booked"))


class Room(models.Model):
    """
    A model to create and manage rooms
    """

    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_owner"
    )
    size = models.IntegerField()
    features = models.CharField(max_length=30, null=False, blank=False)
    description = RichTextField(max_length=10000, null=False, blank=False)
    price = models.IntegerField()
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="imgroomsbooking/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    available_on = models.DateTimeField()
    rating = models.ManyToManyField(User, related_name="room_rate", blank=True)

    class Meta:
        ordering = ["-size"]

    def __str__(self):
        return self.title

    def num_of_rate(self):
        return self.rating.max()


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
