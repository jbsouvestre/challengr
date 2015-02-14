'''
'''
from rest_framework import serializers
from apps.player.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    program = serializers.FileField(max_length=1024 * 1024)

    class Meta:
        model = Player
        fields = ("id", "owner", "type", "name", "created_at",
                  "wins", "losses", "draws", "games")
        read_only_fields = ("wins", "losses", "draws", "games", "created_at", "owner", "type")
