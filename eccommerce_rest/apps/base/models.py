from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('estado', default=True)
    created_date = models.DateField('fecha de modificacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('fecha de modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('fecha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Model Base'
        verbose_name = 'Model Base'
