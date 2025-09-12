from django.urls import path
from main.views import landing_page, create_product, show_product, show_json

app_name = 'main'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product_id'),
    path('product/', show_product, name='show_product'),
    path('json/', show_json, name='show_json'),

]