from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from apps.player.models import Player
from apps.player.serializers import PlayerSerializer
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.account.serializers import UserSerializer

# Create your views here.


class ThisAccount(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated():
            location = reverse("user-detail", (str(request.user.id),))
            return Response(headers={"Location": location}, status=status.HTTP_302_FOUND)
        else:
            return Response({"detail": ["Please re-authenticate"]}, status=status.HTTP_401_UNAUTHORIZED)


class AccountViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
