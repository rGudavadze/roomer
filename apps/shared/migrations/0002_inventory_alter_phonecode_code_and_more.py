# Generated by Django 4.0 on 2023-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Inventory Name', max_length=256, verbose_name='name')),
            ],
        ),
        migrations.AlterField(
            model_name='phonecode',
            name='code',
            field=models.CharField(max_length=255, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='phonecode',
            name='country',
            field=models.CharField(max_length=255, verbose_name='country'),
        ),
    ]
