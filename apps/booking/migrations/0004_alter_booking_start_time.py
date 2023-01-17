# Generated by Django 4.0 on 2023-01-14 17:49

import apps.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(validators=[apps.utils.validators.time_future_validation], verbose_name='start_time'),
        ),
    ]