from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category
from users.models import ArtisanProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def product_list(request):
    """Display all products, optionally filtered by category"""
    category_id = request.GET.get('category')
    products = Product.objects.all().order_by('-created_at')
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories, 'current_category': category_id})

@login_required
def add_product(request):
    try:
        artisan_profile = request.user.artisanprofile
    except ArtisanProfile.DoesNotExist:
        return redirect('dashboard')  # or show an error

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.artisan = artisan_profile
            product.save()
            messages.success(request, f"Product '{product.name}' added successfully!")
            return redirect('products:my_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def my_products(request):
    try:
        artisan_profile = request.user.artisanprofile
        products = Product.objects.filter(artisan=artisan_profile)
    except ArtisanProfile.DoesNotExist:
        products = []
    return render(request, 'products/my_products.html', {'products': products})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, artisan=request.user.artisanprofile)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{product.name}' updated successfully!")
            return redirect('products:my_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, artisan=request.user.artisanprofile)
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f"Product '{product_name}' deleted successfully!")
        return redirect('products:my_products')
    return render(request, 'products/confirm_delete.html', {'product': product})

# Category management views
@login_required
def add_category(request):
    """Add a new category (admin/artisan only)"""
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category = Category.objects.create(name=name)
            messages.success(request, f"Category '{name}' added successfully!")
            return redirect('products:list_categories')
        else:
            messages.error(request, "Category name is required.")
    
    return render(request, 'products/add_category.html')

@login_required
def list_categories(request):
    """Display all categories"""
    categories = Category.objects.all().order_by('name')
    return render(request, 'products/list_categories.html', {'categories': categories})

@login_required
def edit_category(request, pk):
    """Edit an existing category"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category.name = name
            category.save()
            messages.success(request, f"Category '{name}' updated successfully!")
            return redirect('products:list_categories')
        else:
            messages.error(request, "Category name is required.")
    
    return render(request, 'products/edit_category.html', {'category': category})

@login_required
def delete_category(request, pk):
    """Delete a category"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f"Category '{category_name}' deleted successfully!")
        return redirect('products:list_categories')
    
    return render(request, 'products/confirm_delete_category.html', {'category': category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})