from django.contrib import admin
from django.db import models

from models_module.forms.widgets import ImageClearableFileInput


class CustomAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.ImageField: {"widget": ImageClearableFileInput},
    }