from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


@api_view(["GET"])
def getData(request):
    person = {"name": "Marceli"}
    return Response(person)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
