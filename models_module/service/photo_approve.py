from django.utils import timezone


class PhotoApprove:

    @staticmethod
    def photo_update_on_approval(instance):
        from models_module.models.photo.models import Photo
        if instance.__class__ is Photo:
            photo = instance
        if photo.__class__ == 'ModeratedPhoto':
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
            raise Exception('Instance must be of Photo class')

    @staticmethod
    def photo_not_approved(instance):

        photo = instance

        photo.future_image = None
        photo.future_name = None
        photo.future_description = None

        photo.save()
