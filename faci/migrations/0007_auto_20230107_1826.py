# Generated by Django 3.2.10 on 2023-01-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faci', '0006_auto_20230107_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='facicanvas',
            name='key_thoughts',
            field=models.TextField(default='', max_length=10000, verbose_name='Ключевые мысли'),
        ),
        migrations.AddField(
            model_name='facicanvas',
            name='parked_thoughts',
            field=models.TextField(default='', max_length=10000, verbose_name='Парковка'),
        ),
    ]
