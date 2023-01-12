# Generated by Django 4.0 on 2023-01-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('code', models.CharField(max_length=255, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Phone Code',
                'verbose_name_plural': 'Phone Codes',
                'ordering': ['country'],
            },
        ),
    ]
