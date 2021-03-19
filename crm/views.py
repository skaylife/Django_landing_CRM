from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {
        'object_list' : object_list,
        'form' : form
    })

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
