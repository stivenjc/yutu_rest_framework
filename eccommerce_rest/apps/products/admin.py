from django.contrib import admin
from apps.products.models import *


# Register your models here.

class MesaureUNitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


admin.site.register(MeasureUnit, MesaureUNitAdmin)

admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)
