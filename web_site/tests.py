import requests
from django.test import TestCase
from web_site.services.user.create import CreateUser
from web_site.services.photo.upload import CreatePhoto
from models_module.models.user.models import User
from models_module.models.photo.models import Photo


# Test for user creation in user_service
class CreateUserTest(TestCase):

    def test_create_user(self):
        inputs = {
            'email': 'kvothe@edemaruh.com',
            'password': 'do0r$0f$stone42',
            'first_name': 'John',
            'last_name': 'Doe',
        }

        CreateUser.execute(inputs)

        user = User.objects.get()
        self.assertEqual(user.email, inputs['email'])

    def test_create_photo(self):
        inputs = {
            'user': 'admin@email.com',
            'user_id': '1',
            'name': 'some',
            'description': 'dsd',
        }
        files = {
            'image': 'sssssss'
        }
        CreatePhoto.execute(inputs, files=files)

        photo = Photo.objects.get()
        self.assertEqual(photo.owner, inputs['user'])
