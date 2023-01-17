# Generated by Django 4.0 on 2023-01-13 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_user_phone_code_user_phone_number'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID', primary_key=True, serialize=False, verbose_name='id')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At', verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At', verbose_name='updated_at')),
                ('deleted', models.BooleanField(default=False, help_text='Deleted', verbose_name='deleted')),
                ('start_time', models.DateTimeField(verbose_name='start_time')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
                ('status', models.CharField(choices=[('active', 'active'), ('finished', 'finished'), ('cancelled', 'cancelled')], default='active', help_text='Status', max_length=128, verbose_name='status')),
                ('room', models.ForeignKey(help_text='Room', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.room')),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.CheckConstraint(check=models.Q(('end_time__gte', django.db.models.expressions.F('start_time'))), name='start_end_time_check'),
        ),
    ]