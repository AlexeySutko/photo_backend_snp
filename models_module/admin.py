from django.contrib import admin
from django.contrib.auth.models import Group

from models_module.models.user.models import User
from models_module.models.photo.models import Photo
from models_module.admins.user import CustomUserAdmin
from models_module.admins.photo import PhotoAdmin

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.unregister(Group)
