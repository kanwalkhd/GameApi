from django.contrib import admin
from .models import *


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    admin.site.register(Player)


class GameAdmin(admin.ModelAdmin):
    list_display = ('game',)
    admin.site.register(Game)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'game', 'level', 'score')
    admin.site.register(Level)
