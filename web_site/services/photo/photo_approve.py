from django.utils import timezone

class PhotoApprove:
    FIELDS = ['future_name', "future_description", "future_image"]

    @classmethod
    def update(cls, instance, parameter):
        if parameter:
            parameter_without_future = parameter.split('_')[1]
            setattr(instance, parameter_without_future, getattr(instance, parameter))
            setattr(instance, parameter, None)

    @classmethod
    def photo_approved(cls, instance):
        if instance.__class__.__name__ == 'ModeratedPhoto':
            [PhotoApprove.update(instance, parameter) for parameter in cls.FIELDS]
            instance.save()
        else:
            raise Exception(f'{instance.__class__.__name__} is not an instance of a Photo')


    @classmethod
    def photo_not_approved(cls, instance):
        [setattr(instance, parameter, None) for parameter in cls.FIELDS]

        instance.save()
