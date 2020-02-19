from django.db import models
import uuid
from drc.models import Counter


class Pet(models.Model):
    name = models.CharField(max_length=200, null=False)
    image_link = models.URLField(max_length=2000, unique=True)


class PetViewCounter(Counter):
    pass
