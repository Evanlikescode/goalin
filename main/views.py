from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def landing_page(request):

    product_list = Product.objects.all()

    data = {
        'app_name': 'goalin',
        'creator_name': 'Evan Haryo Widodo',
        'creator_class': 'PBP A',
        'product_list' : product_list
    }

    return render(request, "landing_page.html", data)


def create_product(request):

    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:landing_page')

    data = {'form': form}
    return render(request, "create_product.html", data)

def show_product(request, id=None):
    if id is None:
        product_list = Product.objects.all()
        data = {
            'product_list' : product_list
        }
        return render(request, "show_product.html", data)
    
    product = get_object_or_404(Product, pk=id)

    data = {
        'product': product
    }

    return render(request, "more_product.html", data)


def show_json(request):
    news_list = Product.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")