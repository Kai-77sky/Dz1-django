from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.IntegerField(default=3)
    bottles_ordered = models.IntegerField(default=5)
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='photos',
        null=True,
        blank=True,
    )
