from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
#mis modelos
from apps.baseModels import CRidemodel

class User(AbstractUser, CRidemodel):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('correo electronico', max_length=255, blank=True, null=True)
    name = models.CharField('Nombres',max_length=255)
    last_name = models.CharField('Apellidos',max_length=255, blank=True, null=True)
    image = models.ImageField('IMagen de perfil', upload_to='perfil/', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Users'

    USERNAME_FIELD = 'username'
    REQUEST_FIELD = ['email', 'name', 'last_name']



    def __str__(self):
        return f'{self.name} {self.last_name}'