# Generated by Django 4.1 on 2022-08-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
