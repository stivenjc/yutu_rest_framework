""" django models utils"""
from django.db import models


class CRidemodel(models.Model):
    """comparte ride base models"""

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='date time on which the object was created.')

    modified= models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='date time on which the object was last modified.')

    class Meta:
        """opciones de meta"""

        #esto es para es para que no se defina como una tabla, si no cmo una base para crear tablas.
        abstract = True

        get_latest_by = 'created'
        #este es el orden en que va a presentoar los datos de esta tabla cuando se mado a llamr desde la plantilla
        ordering = ['-created','-modified']