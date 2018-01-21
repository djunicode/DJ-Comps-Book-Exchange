from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sap = models.BigIntegerField()
    profile_pic = models.FileField(upload_to="profile pics/")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
