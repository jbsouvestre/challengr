from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError
from django.db.utils import OperationalError

# Create your models here.


PLAYER_TYPES = (("program", "program"),
                ("user", "user"))


def program_file_name(instance, filename):
    return '/'.join(['program', str(instance.id)])


class Player(models.Model):
    owner = models.ForeignKey(User)
    type = models.CharField(max_length=10, choices=PLAYER_TYPES)
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    games = models.PositiveIntegerField(default=0)


def create_default_player(sender, instance, **kwargs):
    i = 0
    while True:
        name = instance.username
        if i > 0:
            name += str(i)
        try:
            Player.objects.create(owner=instance,
                                  type="user",
                                  name=name
                                  )
            return
        except IntegrityError:
            i += 1
        except OperationalError:
            return  # Possibly while running syncdb


# register the signal
post_save.connect(create_default_player, sender=User, dispatch_uid="create_default_player")
