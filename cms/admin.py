from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider

# Тоже самое как и в модуле заказы
class CmsAdmin(admin.ModelAdmin):
    # Для основной страницы
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_image') # Вывод значений, и вызов функции get_image
    list_display_links = ('cms_title',) # Кликабельность поля
    list_editable = ('cms_css',) # И возможность изменить css прямо в списке

    # Для подробнее
    fields = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    readonly_fields = ('get_img',)

    # Функция для вывода картинки
    def get_image(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'Нет картинки'

    # Для карточки
    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="300px"')
        else:
            return 'Нет картинки'

    get_image.short_description = 'Миниатюра' # Перименование get_image на Миниатюра
    get_img.short_description = 'Миниатюра' # Тоже самое, только для карточки

admin.site.register(CmsSlider, CmsAdmin)