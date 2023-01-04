from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):
    game = models.CharField(max_length=50)

    def __str__(self):
        return self.game


class Level(models.Model):
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE, default="puzzle")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    level = models.IntegerField()
    score = models.IntegerField()
