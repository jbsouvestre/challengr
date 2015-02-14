from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from apps.player.models import Player
from apps.player.serializers import PlayerSerializer
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.core.exceptions import ValidationError

# Create your views here.


class PlayerViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def pre_save(self, obj):
        if obj.id is not None and obj.owner != self.request.user:
            raise ValidationError({"details": [_("You cannot modify someone else's player")]})

        obj.owner = self.request.user
