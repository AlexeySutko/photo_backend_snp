from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.services.user.details import GetUserDetailsService
from API.serializers.user_serializer import UserSerializer


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        outcome = GetUserDetailsService.execute({
            'user_id': request.user.id
        })
        serializer = UserSerializer(outcome.result)
        return Response(serializer.data)
