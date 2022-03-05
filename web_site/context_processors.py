from .forms.user.login import CustomUserLoginForm
from .forms.user.registration import CustomUserRegistrationForm
from .forms.user.change import CustomUserChangeForm

from .services.like.is_liked import IsLiked


def access_login_form(request):
    form = CustomUserLoginForm
    return {'login_form': form}


def access_registration_form(request):
    form = CustomUserRegistrationForm
    return {'registration_form': form}


def access_change_form(request):
    form = CustomUserChangeForm
    return {'change_form': form}