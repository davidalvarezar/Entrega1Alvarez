# Generated by Django 4.1.1 on 2022-11-02 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Mensajeria', '0003_canal_canalmensaje_canalusuario_delete_mensaje_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='displayusername',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]