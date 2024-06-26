# Generated by Django 5.0.6 on 2024-05-28 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bars', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='bar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bars.bar'),
        ),
    ]
