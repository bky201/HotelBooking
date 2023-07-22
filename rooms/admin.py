from django.contrib import admin
from .models import Room, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = (

#     )
