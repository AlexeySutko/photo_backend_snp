from django import forms
from service_objects.services import Service
from models_module.models.user.models import User


"""
Service layer for logic related to creating users
"""


class CreateUser(Service):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(max_length=50)

    def process(self):
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        password = self.cleaned_data['password']

        self.user = User.objects.create_user(username=email, email=email, password=password,
                                             first_name=first_name, last_name=last_name)

        return self.user