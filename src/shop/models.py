from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name_uz
