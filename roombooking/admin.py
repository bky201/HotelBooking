from django.contrib import admin
from .models import Room, Comment


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "size",
        "features",
        "description",
        "status",
        "available_on",
    )
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "available_on")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "room", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
