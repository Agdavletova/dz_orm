from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == "name":
        phones = sorted(list(Phone.objects.values()), key=lambda x:x['name'])
        print(phones)
    elif sort == 'max_price':
        phones = sorted(list(Phone.objects.values()), key=lambda x: x['price'], reverse=True)
    else:
        phones = sorted(list(Phone.objects.values()), key=lambda x: x['price'])
    context = {
        "phones":phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone =  get_object_or_404(Phone, slug=slug)
    context = {
        'phone':phone
    }
    return render(request, template, context)
