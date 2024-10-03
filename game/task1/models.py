from django.db import models


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    first_login = models.DateTimeField(auto_now_add=True)
    bonuses = models.ManyToManyField(
        "Boost", blank=True, related_name="bonuses"
    )


class BoostType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Boost(models.Model):
    id = models.BigAutoField(primary_key=True)
    effect = models.ForeignKey(
        "BoostType", on_delete=models.PROTECT
    )
    duration = models.IntegerField()
    power = models.IntegerField()

