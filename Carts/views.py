from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from Services.models import ItemModel, ServiceModel
from Carts.models import CartItemModel, CartServiceModel


@login_required
def cartView(request):
    cart_items = CartItemModel.objects.filter(userId=request.user)
    cart_services = CartServiceModel.objects.filter(userId=request.user)
    
    total_price = sum(item.itemId.price for item in cart_items) + \
                 sum(service.serviceId.price for service in cart_services)
    
    context = {
        'cart_items': cart_items,
        'cart_services': cart_services,
        'total_price': total_price,
    }
    return render(request, 'Carts/cart.html', context)


@login_required
def addToCartItemView(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    CartItemModel.objects.get_or_create(
        userId=request.user,
        itemId=item
    )
    messages.success(request, f'Товар "{item.name}" добавлен в корзину')
    return redirect('cart')


@login_required
def addToCartService(request, pk):
    service = get_object_or_404(ServiceModel, pk=pk)
    if request.method == 'POST':
        date_visit = request.POST.get('date')
        CartServiceModel.objects.create(
            userId=request.user,
            serviceId=service,
            dateVisit=date_visit
        )
        messages.success(request, f'Услуга "{service.name}" добавлена в корзину')
        return redirect('cart')
    return redirect('service_detail', pk=pk)

@login_required
def removeFromCartItem(request, pk):
    cart_item = get_object_or_404(CartItemModel, pk=pk, userId=request.user)
    cart_item.delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect('cart')


@login_required
def removeFromCartService(request, pk):
    cart_service = get_object_or_404(CartServiceModel, pk=pk, userId=request.user)
    cart_service.delete()
    messages.success(request, 'Услуга удалена из корзины')
    return redirect('cart')

@login_required
def checkoutView(request):
    return redirect('index')