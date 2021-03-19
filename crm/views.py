from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()
    dict_obj = {
        'slider_list' : slider_list,
        'pc_1' : pc_1,
        'pc_2' : pc_2,
        'pc_3' : pc_3,
        'price_table' : price_table
    }

    return render(request, './index.html', dict_obj)

def thanks_page(request):
    name = request.POST['name'] # Без информации в в адресной строке
    phone = request.POST['phone'] # POST
    # name = request.GET['name'] # Метод отправки формы с информацие в адресной строке
    # phone = request.GET['phone'] # GET
    element = Order(order_name=name, order_phone=phone)
    element.save()
    # name = request.GET.get('name') # Alt
    # phone = request.GET.get('phone') # Alt
    return render(request, './thanks_page.html', {
        'name' : name,
        'phone' : phone
    })
