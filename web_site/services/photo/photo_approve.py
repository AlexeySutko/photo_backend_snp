import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from photo_backend_snp.settings import REDIS_INSTANCE


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
            cls._send_notification(photo=instance, state_message="approved")
            instance.save()
        else:
            raise Exception(f'{instance.__class__.__name__} is not an instance of a Photo')

    @classmethod
    def photo_not_approved(cls, instance):
        [setattr(instance, parameter, None) for parameter in cls.FIELDS]
        cls._send_notification(photo=instance, state_message="not approved")
        instance.save()

    @classmethod
    def _send_notification(cls, photo, state_message):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(REDIS_INSTANCE.get(f"private_for_{photo.owner_id}").decode("utf-8"), {
            "type": "photo_approval_notification",
            "payload": json.dumps({
                'type': "photo_approval",
                'photo_name': photo.name,
                'status': state_message,
            }),
        })
