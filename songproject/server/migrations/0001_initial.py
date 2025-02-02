# Generated by Django 5.1.5 on 2025-02-01 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('danceability', models.FloatField(default=0)),
                ('energy', models.FloatField(default=0)),
                ('key', models.IntegerField(default=0)),
                ('loudness', models.FloatField(default=0)),
                ('mode', models.IntegerField(default=0)),
                ('acousticness', models.FloatField(default=0)),
                ('instrumentalness', models.FloatField(default=0)),
                ('liveness', models.FloatField(default=0)),
                ('valence', models.FloatField(default=0)),
                ('tempo', models.FloatField(default=0)),
                ('duration_ms', models.IntegerField(default=0)),
                ('time_signature', models.IntegerField(default=0)),
                ('num_bars', models.IntegerField(default=0)),
                ('num_sections', models.IntegerField(default=0)),
                ('num_segments', models.IntegerField(default=0)),
                ('song_class', models.IntegerField(default=0)),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.songrating')),
            ],
        ),
        migrations.CreateModel(
            name='SongUserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.song')),
            ],
        ),
    ]
