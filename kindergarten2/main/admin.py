from django.contrib import admin
from .models import *


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'content']


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'position']


@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'text']
