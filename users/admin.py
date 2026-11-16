from users.models import Profile
from django.contrib import admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'photo', 'date_birth']
    list_editable = ['date_birth']
    list_display = ('user', 'photo', 'date_birth')