from django.db import models

class PriceCard(models.Model):
    pc_title = models.CharField(max_length=20, verbose_name='Название услуги')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')
    pc_value = models.CharField(max_length=20, verbose_name='Цена')

    def __str__(self):
        return self.pc_value


    class Meta:
        verbose_name = 'Название пакета услуг'
        verbose_name_plural = 'Название пакета услуг'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Название услуги')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая цена')


    def __str__(self):
        return self.pt_title


    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'