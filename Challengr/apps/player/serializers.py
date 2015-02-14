'''
'''
from rest_framework import serializers
from apps.player.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ("id", "owner", "type", "name", "created_at",
                  "wins", "losses", "draws", "games")
