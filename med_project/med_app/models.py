from django.db import models

# Create your models here.
class Pokemmon(models.Model):
  name = models.CharField
  hp = models.IntegerField()