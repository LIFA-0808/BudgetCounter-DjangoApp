from django.db import models
from datetime import date


class Record(models.Model):
    """"New budget record"""
    class Item(models.TextChoices):
        INCOME = 'income', 'Текущие доходы'
        EXPENSES = 'expenses', 'Текущие расходы'
        WISHLIST = 'wish_list', 'Лист желаний'

    budget_item = models.CharField(
        max_length=9,
        choices=Item.choices,
        default=Item.INCOME,
        verbose_name='Статья бюджета'
    )

    money = models.FloatField(verbose_name='Размер')
    item_description = models.CharField(max_length=200, verbose_name='Описание')
    date_added = models.DateField(default=date.today, verbose_name='Дата')

    def __str__(self):
        """Returns the stream representation of the model"""
        return ' - '.join([str(self.money), self.item_description])

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
