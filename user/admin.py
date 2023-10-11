from django.contrib import admin
from user.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']

admin.site.register(User, UserAdmin)
