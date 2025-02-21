from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reg_number', 'location', 'birth_date')

admin.site.register(Profile, ProfileAdmin)
