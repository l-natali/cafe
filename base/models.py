import os.path

from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_filename(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_filename)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class Event(models.Model):

    def get_file(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events/', new_filename)

    name = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to=get_file)

    def __str__(self):
        return f'{self.name}'


class Gallery(models.Model):

    def get_file(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery/', new_filename)

    position = models.SmallIntegerField(unique=True)
    img = models.ImageField(upload_to=get_file)

    class Meta:
        ordering = ('position', )


class About(models.Model):

    def get_file(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=5000)
    img = models.ImageField(upload_to=get_file)

    def __str__(self):
        return f'{self.title}'


class WhyUs(models.Model):
    num_reason = models.SmallIntegerField(unique=True)
    title = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('num_reason', )


