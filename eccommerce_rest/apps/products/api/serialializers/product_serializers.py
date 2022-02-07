from apps.products.models import Product

from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']

    def validate_measure_unit(self, value):
        """
        esto es para hacer uan validacion de que llege el valor del campo measure_unit,
         colocamos primero validate_ seguido del campo que deseemos validar en este caso es measure_unit
        """
        if value == '' or value == None:
            raise serializers.ValidationError('debes ingresar una unidad de medida')
        return value

    def validate_category_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('debes ingresar una categoria de producto')
        return value

    def validate(self, data):
        """
        esto es para calidar que la llave del valor llega ejemplo
         {"measure_unit": ""], aqui no estoy validando lo que llega como valor del campo solo lo que llega como keys()
        """
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({
                'measure:unit': 'debes ingresar un aunidad de medida'
            })

        if 'category_product' not in data.keys():
            raise serializers.ValidationError({
                'category_product': 'debes ingresar una categorya de product'
            })

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'name': instance.name,
            'image': instance.image.url if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }
