from django.db import models

class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_date_time = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name= 'Имя')
    order_phone = models.CharField(max_length=200, verbose_name= 'Телефон')
    # Поле привязки PROTECT - Запрет удаления полей. Null = True разрешение пусты миграции в базе данных. Blank = True - для пусты в полях админики
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class CommentCrm(models.Model):
    # К родительскому классу Order, используется удаление по CASCADE'у, если удалится родитель, значит удалится и comment_binding
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


