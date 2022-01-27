# Generated by Django 4.0.1 on 2022-01-27 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
