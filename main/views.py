import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages

# Create your views here.
@login_required(login_url="/login")
def landing_page(request):

    product_list = Product.objects.all()

    data = {
        'app_name': 'goalin',
        'creator_name': 'Evan Haryo Widodo',
        'creator_class': 'PBP A',
        'creator_npm': '2406435824',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')

    }

    return render(request, "landing_page.html", data)

@login_required(login_url="/login")
def create_product(request):

    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:landing_page')

    data = {
        "form": form,
        "form_action": reverse("main:create_product"),
        "button_label": "Create",
        "form_title": "Create Product",
    }
    return render(request, "product_form.html", data)

@login_required(login_url="/login")
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:landing_page')

    data = {
        "form": form,
        "product": product,
        "form_action": reverse("main:edit_product", args=[product.id]),
        "button_label": "edit",
        "form_title": "Edit Product",
    }
    return render(request, "product_form.html", data)


@login_required(login_url="/login")
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:landing_page'))


@login_required(login_url="/login")
def show_product(request, id=None):
    if id is None:
        filter_type = request.GET.get("filter", "all")  

        if filter_type == "all":
            product_list = Product.objects.all()
        else:
            product_list = Product.objects.filter(user=request.user)
        data = {
            'product_list' : product_list
        }
        return render(request, "show_product.html", data)
    
    product = get_object_or_404(Product, pk=id)

    data = {
        'product': product
    }

    return render(request, "more_product.html", data)

@login_required(login_url="/login")
def show_product_json(request, id=None):
    if id is None:
        product_list = Product.objects.all()
        json_data = serializers.serialize("json", product_list)
        return HttpResponse(json_data, content_type="application/json")
    
    product = Product.objects.filter(pk=id)
    json_data = serializers.serialize("json", product)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url="/login")
def show_product_xml(request, id=None):
    if id is None:
        product_list = Product.objects.all()
        json_data = serializers.serialize("xml", product_list)
        return HttpResponse(json_data, content_type="application/xml")
    
    product = Product.objects.filter(pk=id)
    json_data = serializers.serialize("xml", product)
    return HttpResponse(json_data, content_type="application/xml")
    


def register_user(request):
    form = UserCreationForm()   


    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "msg": "Your account has been successfully created!"
            })
        else:
            return JsonResponse({
                "success": False,
                "msg": form.errors
            })
    
    form = UserCreationForm()
    data = {
        "form": form
    }

    return render(request, "register.html", data)

def login_user(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                "success": True,
                "msg": "Successfully Login!"
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                "success": False,
                "msg": "Please check your username and password again!"
            })
    
    form = AuthenticationForm(request)
    
    data = {
        'form': form
    }

    return render(request, 'login.html', data)

@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    response.delete_cookie('last_login')
    return response