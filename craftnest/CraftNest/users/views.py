from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from users.froms import RegisterForm


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user=form.save(commit=False)
            # login(request, user)  #Auto login after register
            user.is_artisan=form.cleaned_data.get('is_artisan')
            user.save()
            messages.success(request, "Successfully Registered")
            return redirect('home')
        else:
            messages.error(request, "Registration Failed:Please correct the error below.")
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Login Failed:Please correct the error below.")

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def artisan_dashboard(request):
    if not request.user.is_artisan:
        return redirect('home')

    products = Product.objects.filter(artisan=request.user.artisanprofile)

    return render(request, 'users/dashboard.html',
                  {'user': request.user, 'products': products })


