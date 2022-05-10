from service_objects.services import Service, forms

from models_module.models import User


class GetUserDetailsService(Service):
    user_id = forms.IntegerField(required=True, min_value=1)

    def process(self):
        self.result = self._get_user_by_id()

        return self

    def _get_user_by_id(self):
        user = User.objects.get(id=self.cleaned_data.get('user_id'))

        return user
