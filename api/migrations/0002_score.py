# Generated by Django 4.1.5 on 2023-01-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
