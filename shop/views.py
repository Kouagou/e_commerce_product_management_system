from rest_framework import viewsets
from .models import Product, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from .forms import ProductForm, CategoryForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def products_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)


def product_index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'products': products, 'categories': categories})


def product_show_create_page(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_index')
    else:
        form = ProductForm()
    return render(request, 'product/new.html', {'form': form})


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit.html', {'form': form, 'product': product})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_index')


def category_index(request):
    categories = Category.objects.all()
    return render(request, 'category/index.html', {'categories': categories})


def category_show_create_page(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_index')
    else:
        form = CategoryForm()
    return render(request, 'category/new.html', {'form': form})


def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_index')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/edit.html', {'form': form, 'category': category})


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_index')
