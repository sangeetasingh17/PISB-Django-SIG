from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    gender = models.CharField(max_length=6, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    def __str__(self):
        return f'{self.user.username}'
