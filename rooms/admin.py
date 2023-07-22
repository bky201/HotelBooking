from django.contrib import admin
from .models import Room, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'available_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'available_on')
    summernote_fields = ('content')

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = (

#     )
