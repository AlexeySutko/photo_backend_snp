from rest_framework import serializers

from models_module.models import Photo, User


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, min_value=1)
    name = serializers.CharField()
    description = serializers.CharField()
    publish_date = serializers.DateTimeField()
    image = serializers.ImageField()
    likes_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()

    # class Meta:
    #     model = Photo
    #     fields = (
    #         "id",
    #         "name",
    #         "description",
    #         "publish_date",
    #         "image",
    #     )
