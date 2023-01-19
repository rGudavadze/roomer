# Generated by Django 4.0 on 2023-01-19 22:00

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_helpers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False, verbose_name='id')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At', verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At', verbose_name='updated_at')),
                ('deleted', models.BooleanField(default=False, help_text='Deleted', verbose_name='deleted')),
                ('name', models.CharField(help_text='Room Name', max_length=256, verbose_name='name')),
                ('seats', models.IntegerField(help_text='Number of seats', validators=[django.core.validators.MinValueValidator(1)], verbose_name='seats')),
                ('inventories', models.ManyToManyField(help_text='Inventories', to='app_helpers.Inventory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
