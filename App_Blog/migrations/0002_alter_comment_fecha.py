# Generated by Django 4.1.1 on 2022-10-31 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
