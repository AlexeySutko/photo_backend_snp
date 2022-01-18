from django.test import TestCase
from web_site.services.user.create import CreateUser
from models_module.models.user.models import User


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
