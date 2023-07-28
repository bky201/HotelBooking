from django.contrib import admin
from .models import Room, Booking, Comment, About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ("title", "content")
    search_fields = ["title", "content"]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ("user", "room", "check_in", "check_out")
    search_fields = ["user", "room", "check_in", "check_out"]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "number",
        "slug",
        "features",
    )
    search_fields = ["title", "number"]
    prepopulated_fields = {"slug": ("title", "number")}
    list_filter = ("title", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "room", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
