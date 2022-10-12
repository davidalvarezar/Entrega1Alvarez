# Generated by Django 4.1 on 2022-10-10 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Mensajeria', '0005_canalmensajes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canalmensajes',
            name='usuario',
        ),
        migrations.AddField(
            model_name='canalmensajes',
            name='usuarios',
            field=models.ManyToManyField(blank=True, related_name='threads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emisor',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]