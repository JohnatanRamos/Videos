from django.db import models

# importamos la clase User
from django.contrib.auth.models import User


class Profile(models.Model):
    # user es la foreing key, y la pk de User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    webpage = models.URLField(max_length=200)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='profile/images', blank=True, null=True)

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

