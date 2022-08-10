# Generated by Django 4.1 on 2022-08-10 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_about_event_gallery_whyus'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone in format xxx xxx xxxx', regex='^(\\d{3}[- ]?){2}\\d{4}$')])),
                ('persons', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Email in format xxxxxx@xx.xx', regex='^[^-_][a-zA-Z0-9_-]+@\\w+\\.\\w+$')])),
                ('book_date', models.DateField()),
                ('book_time', models.TimeField()),
            ],
            options={
                'ordering': ('-date', '-is_processed'),
            },
        ),
    ]
