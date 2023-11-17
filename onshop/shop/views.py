from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

def show_product(request):

    x = Products.objects.all()
    item_name = request.GET.get("item_name", "").strip()
    
    if item_name:
        product_object = x.filter(title__icontains=item_name)
    else:
        product_object = x

    # Now, it shows on which object or list we have to apply it and how many products to show at a time.
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/Product_detail.html', {'x': product_object})
