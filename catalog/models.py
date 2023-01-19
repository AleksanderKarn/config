from django.db import models
from datetime import date
# Create your models here.


NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name_product = models.CharField("Имя", max_length=250)
    description = models.TextField("Описание", default=0)
    image = models.ImageField("Изображение", upload_to='products/', **NULLABLE)
    category_name = models.CharField(max_length=50)
    unit_price = models.IntegerField(default=0)
    create_date = models.DateField("Дата создания", default=date.today)
    change_date = models.DateField("Дата изменения", default=date.today)

    def __str__(self):
        return f'{self.id} {self.name_product} {self.unit_price} {self.category_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Category(models.Model):
    category_name = models.CharField("Имя категории",max_length=50)
    description = models.TextField("Описание", default=0)

    def __str__(self):
        return f'{self.id} {self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'