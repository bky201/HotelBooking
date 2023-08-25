# rating_filters.py

from django import template
from django.db.models import Avg
from ..models import Review

register = template.Library()


@register.filter
def average_rating(room):
    return Review.objects.filter(room=room).aggregate(Avg("rating"))["rating__avg"]
