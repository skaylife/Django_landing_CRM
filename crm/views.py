from django.shortcuts import render
from .models import Order

def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {
        'object_list' : object_list
    })

def thanks_page(request):
    return render(request, './thanks_page.html')
