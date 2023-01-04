from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game']


class LevelSerializer(serializers.ModelSerializer):
    # user_id = serializers.StringRelatedField(read_only=True)
    # game = serializers.StringRelatedField(read_only=True )

    class Meta:
        model = Level
        fields = ['id', 'user_id', 'game', 'level', 'score']

    def to_representation(self, instance):
        rep = super(LevelSerializer, self).to_representation(instance)
        rep['game'] = instance.game.game
        return rep
