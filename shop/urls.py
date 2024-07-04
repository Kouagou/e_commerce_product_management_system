from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, products_by_category
from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', views.product_index, name='product_index'),
    path('products/', views.product_index, name='product_index'),
    path('products/new/', views.product_show_create_page, name='product_show_create_page'),
    path('products/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),

    path('categories/', views.category_index, name='category_index'),
    path('categories/new/', views.category_show_create_page, name='category_show_create_page'),
    path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),

    path('api/', include(router.urls)),
    path('api/categories/<int:category_id>/products', products_by_category, name='products_by_category'),
]
