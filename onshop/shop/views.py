from django.shortcuts import render
from .models import Products


def show_product(request):

    x=Products.objects.all()
    return render(request,'shop/Product_detail.html',{'x':x})

