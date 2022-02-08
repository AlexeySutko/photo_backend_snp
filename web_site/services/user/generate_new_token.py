from rest_framework.authtoken.models import Token


def generate_new_token(request):
    Token.objects.filter(user=request.user).delete()
    Token.objects.create(user=request.user)
