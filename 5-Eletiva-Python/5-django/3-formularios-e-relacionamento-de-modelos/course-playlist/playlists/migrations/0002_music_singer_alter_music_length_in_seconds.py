# Generated by Django 5.0.1 on 2024-01-29 21:08

import django.db.models.deletion
import playlists.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playlists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="singer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="musics",
                to="playlists.singer",
            ),
        ),
        migrations.AlterField(
            model_name="music",
            name="length_in_seconds",
            field=models.IntegerField(
                validators=[playlists.validators.validate_music_length]
            ),
        ),
    ]
