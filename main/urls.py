from django.urls import path
from main.views import landing_page, create_product, show_product, show_product_json, show_product_xml, register_user, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('create-product/', create_product, name='create_product'),
    path('product/', show_product, name='show_product'),
    path('product/<str:id>/', show_product, name='show_product_id'),
    path('json/product/', show_product_json, name='show_product_json'),
    path('json/product/<str:id>/', show_product_json, name='show_product_json_id'),
    path('xml/product/', show_product_xml, name='show_product_xml'),
    path('xml/product/<str:id>/', show_product_xml, name='show_product_xml_id'),

    path('register/', register_user, name="register_user" ),
    path('login/', login_user, name="login_user" ),
    path('logout/', logout_user, name="logout_user" ),
]