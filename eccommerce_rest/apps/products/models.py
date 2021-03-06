from django.db import models

from apps.base.models import BaseModel


# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    description = models.CharField('description', max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.description


class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='indicador de ofertas')

    class Meta:
        verbose_name = 'indicador de oferta'
        verbose_name_plural = 'indicador de ofertas'

    def __str__(self):
        return f" Oferta de la categoria {self.category_product} : {self.descount_value}%"


class Product(BaseModel):
    name = models.CharField('nombre de producto', max_length=150, unique=True, blank=False, null=False)
    description = models.CharField('description de producto', max_length=200, blank=False, null=False)
    image = models.ImageField('imagen de producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
