# Generated by Django 5.0.1 on 2024-01-30 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Music",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("recorded_at", models.DateField()),
                ("length_in_seconds", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Singer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "musics",
                    models.ManyToManyField(related_name="playlists", to="core.music"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="music",
            name="singer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="musics",
                to="core.singer",
            ),
        ),
    ]
