# Generated by Django 4.1.5 on 2023-01-03 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_game_game_game_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='Game_Name',
            new_name='game',
        ),
    ]
