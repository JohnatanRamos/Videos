from django.db import models
"""Se instancia el modulo de models"""


# Significa que user es un modelo de Django
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)

    # Instanciamos la clase EmailField del modulo de models

    name = models.CharField(max_length=42)
    phone = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    birthdate = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    # actualiza en la creación
    modified = models.DateTimeField(auto_now=True)
    # actualiza cada vez que se haga un cambio
    admin = models.BooleanField(default=False)

