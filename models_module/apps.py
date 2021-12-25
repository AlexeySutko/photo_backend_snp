from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModelsModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models_module'
    verbose_name = _("models")
