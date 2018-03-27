from django.db import models
from django.contrib.auth.models import User

image_url = "/media/profile%20pics/default_user.png"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sap = models.BigIntegerField(unique=True)
    profile_pic = models.FileField(upload_to="profile pics/", default="default_user.png")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
