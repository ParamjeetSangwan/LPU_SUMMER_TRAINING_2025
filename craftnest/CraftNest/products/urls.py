from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Product listing
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Artisan product management
    path('add/', views.add_product, name='add_product'),
    path('my-products/', views.my_products, name='my_products'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    
    # Category management
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
]
