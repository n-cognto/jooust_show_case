# admin.py
from django.contrib import admin
from .models import News, Event, Notice, Media, PartnerLogo, SchoolActivity

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'featured', 'is_active')
    list_filter = ('featured', 'is_active', 'created_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'is_active')
    list_filter = ('is_active', 'event_date')
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('created_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_date', 'expiry_date', 'is_active')
    list_filter = ('priority', 'is_active', 'created_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'created_date', 'is_active')
    list_filter = ('media_type', 'is_active', 'created_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'is_active')
    list_filter = ('is_active', 'created_date')
    search_fields = ('name',)
    readonly_fields = ('created_date',)

@admin.register(SchoolActivity)
class SchoolActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active')
    list_filter = ('is_active', 'created_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_date',)