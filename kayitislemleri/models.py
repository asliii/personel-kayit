from django.db import models
from django.utils import timezone

class Position(models.Model):
    name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Personel(models.Model):
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=5)
    created_date = models.DateTimeField(
        default=timezone.now)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    def publish(self):
        self.save()

    def __str__(self):
        return self.fullName

