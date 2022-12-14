# Generated by Django 4.1 on 2022-08-08 16:25

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('description', models.TextField(max_length=5000)),
                ('img', models.ImageField(upload_to=base.models.About.get_file)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=3)),
                ('description', models.TextField(max_length=1000)),
                ('img', models.ImageField(upload_to=base.models.Event.get_file)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(unique=True)),
                ('img', models.ImageField(upload_to=base.models.Gallery.get_file)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_reason', models.SmallIntegerField(unique=True)),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ('num_reason',),
            },
        ),
    ]
