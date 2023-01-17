# Generated by Django 4.0 on 2023-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_inventory_alter_phonecode_code_and_more'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.AlterField(
            model_name='room',
            name='inventories',
            field=models.ManyToManyField(help_text='Inventories', to='shared.Inventory'),
        ),
    ]
