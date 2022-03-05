from django.utils import timezone

class PhotoApprove:

    @staticmethod
    def photo_update_on_approval(instance):
        photo = instance
        if photo.__class__.__name__ == 'ModeratedPhoto':
            if photo.future_name is not None:
                photo.name = photo.future_name
                photo.future_name = None
            if photo.future_image is not None:
                photo.image = photo.future_image
                photo.future_image = None
            if photo.future_description is not None:
                photo.description = photo.future_description
                photo.future_description = None

            photo.change_date = timezone.now()

            photo.save()
        else:
            raise Exception(f'{photo.__class__.__name__} is not an instance of a Photo')

    @staticmethod
    def photo_not_approved(instance):

        photo = instance

        photo.future_image = None
        photo.future_name = None
        photo.future_description = None

        photo.save()
