from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог продуктов'
    }
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    product_list = Product.objects.get(pk=pk)
    print(product_list)
    context = {
        'object': product_list,
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}):  {message}')
    return render(request, 'catalog/contacts.html')
