# Generated by Django 2.2.19 on 2021-02-24 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda1',
            name='Stock_Tienda',
        ),
        migrations.RemoveField(
            model_name='tienda2',
            name='Stock_Tienda',
        ),
        migrations.RemoveField(
            model_name='tienda3',
            name='Stock_Tienda',
        ),
        migrations.RemoveField(
            model_name='tienda4',
            name='Stock_Tienda',
        ),
    ]