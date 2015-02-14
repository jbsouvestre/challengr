from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from apps.player.models import Player
from apps.player.serializers import PlayerSerializer
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from utils.files import write_file

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
            raise ValidationError({"details": ["You cannot modify someone else's player"]})

        obj.owner = self.request.user

        if "program" in self.request.FILES:

            obj.type = "program"
        else:
            obj.type = "user"

    def post_save(self, obj, created):
        if obj.type == "program":
            write_file("program/{}".format(obj.id), self.request.FILES["program"])
