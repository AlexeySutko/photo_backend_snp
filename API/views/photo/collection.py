from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from API.serializers.photo_serializer import PhotoSerializer
from API.services.photo.get_collection import GetPhotoCollectionService
from models_module.models import Photo


class PhotoCollectionView(APIView):

    def get(self, request):
        outcome = GetPhotoCollectionService.execute(dict(request.GET.items()))
        serializer = PhotoSerializer(outcome.result, many=True)
        return Response(serializer.data)
