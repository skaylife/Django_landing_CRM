from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Добавление поля комментарий к подробной карточке товара
class Comment(admin.StackedInline):
    model = CommentCrm # Обязательный атрибут
    fields = ('comment_text', 'comment_date') # Какие поля нужно прибавить к карточке подробнее
    readonly_fields = ('comment_date', ) # Это поле доступно только для чтения
    extra = 0 # Для того чтобы отменить стандратную модель поведния Django, тоесть default = 3 | значит три поля для вывода комментария | extra = 0 - значит скрыть поле, и добавить кнопку.

# Добавление во вкладку заказы дополнительных полей = ID ИМЯ ТЕЛЕФОН СТАТУС ВРЕМЯ - ORDER DATE TIME
class OrderAdm(admin.ModelAdmin):
    # Настройка полей на странице заказы
    list_display = ('id',  'order_name', 'order_phone', 'order_status', 'order_date_time') # Добавление полей
    list_display_links = ('id', 'order_name') # Возможность кликнуть, не только по ID но и по ИМЕНИ
    search_fields =  ('order_name', 'order_phone') # Поиск имени и по телефону
    list_filter = ('order_status',) # Сортировка по статусу
    list_editable = ('order_status', 'order_phone',) # Редактирование поля Статус и телефон, нельзя доавить поле имя, так как оно используется для клика. Чтоб изменять поле ИМЯ, нужно убрать его в аргументах {list_display_links}
    list_per_page = 5 # Количество заявок на странице
    list_max_show_all = 100 # Максимально доступное количество заказов для показа на одной странице

    # Настройка полей для отдельной карточки
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_date_time', ) # Порядок вывода информации на карточке заказа подробно
    readonly_fields = ('id', 'order_date_time') # Во избежание ошибки связанных с временем и ID, нужно сделать их доступными для чтения

    # Поле класса комментарий
    inlines = (Comment,) # Обязательный атрибут

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)