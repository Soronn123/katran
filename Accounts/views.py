from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Accounts.forms import RegistrationForm, LoginForm, ProfileForm
from Services.models import ItemModel, ServiceModel
from Carts.models import CartItemModel, CartServiceModel

def indexView(request):
    products = ItemModel.objects.all()[:8]
    services = ServiceModel.objects.all()[:3]
    
    context = {
        'products': products,
        'services': services,
    }
    return render(request, 'index.html', context)

def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('profile')
    else:
        form = RegistrationForm()
    
    return render(request, 'Accounts/register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('profile')
    else:
        form = LoginForm()
    
    return render(request, 'Accounts/login.html', {'form': form})

@login_required
def logoutView(request):
    logout(request)
    messages.info(request, 'Вы успешно вышли из системы.')
    return redirect('index')

@login_required
def profileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    cart_items = CartItemModel.objects.filter(userId=request.user)
    cart_services = CartServiceModel.objects.filter(userId=request.user)
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'cart_services': cart_services,
    }
    return render(request, 'Accounts/profile.html', context)

def aboutView(request):
    return render(request, 'Accounts/about.html')