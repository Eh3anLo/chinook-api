# Generated by Django 5.0 on 2024-08-17 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='track.genre'),
        ),
        migrations.AlterField(
            model_name='track',
            name='track_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
