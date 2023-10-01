
from django import views
from django.urls import path
from .views import Inventory_list, delete_inventory, per_product_view,add_product, update_inventory


app_name = 'myapp'

urlpatterns = [
    path("", Inventory_list, name="Inventory_list"),
    # path("product/<pk>", per_product_view, name="per_product"),
    path("product/<pk>", per_product_view.as_view(), name="per_product"), 
    path("add_inventory/",add_product, name="add_inventory"),
    # path("delete/", delete_inventory.as_view(), name="delete_inventory"),    
    # path("delete/<pk>", delete_inventory, name="delete_inventory"),
     path('delete_inventory/<int:pk>/', delete_inventory, name='delete_inventory'),
     path('update/<int:pk>/', update_inventory, name='update_inventory'),
]