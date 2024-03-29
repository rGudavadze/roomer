# Generated by Django 4.0 on 2023-01-19 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Inventory Name', max_length=256, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('code', models.CharField(max_length=255, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Phone Code',
                'verbose_name_plural': 'Phone Codes',
                'ordering': ['country'],
            },
        ),
    ]
