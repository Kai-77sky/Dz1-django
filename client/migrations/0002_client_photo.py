# Generated by Django 4.1.1 on 2022-09-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]
