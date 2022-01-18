from .forms.user.login import CustomUserLoginForm
from .forms.user.registration import CustomUserRegistrationForm


def access_login_form(request):
    form = CustomUserLoginForm
    return {'login_form': form}


def access_registration_form(request):
    form = CustomUserRegistrationForm
    return {'registration_form': form}
