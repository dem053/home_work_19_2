from datetime import date

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    prod_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', default='описание отсутствует')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    date_created = models.DateField(verbose_name='дата создания', default=date.today)
    date_change = models.DateField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.prod_name} - {self.price} : {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('prod_name',)

