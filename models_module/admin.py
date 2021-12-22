from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from .admins.user import CustomUserAdmin


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
