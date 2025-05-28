"""
URL configuration for Katran project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.asView(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

import Accounts.views as AccountViews
import Carts.views as CartViews
import Services.views as ServiceViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path("", AccountViews.indexView, name='index'),
    path('about/', AccountViews.aboutView, name='about'),   
     
    path('products/<int:pk>/', ServiceViews.itemDetailView, name='item_detail'),
    path('services/<int:pk>/', ServiceViews.serviceDetailView, name='service_detail'),
    path('products/', ServiceViews.productsView, name='products'),
    path('services/', ServiceViews.servicesView, name='services'),

    path('cart', CartViews.cartView, name="cart"),
    path('cart/add/item/<int:pk>/', CartViews.addToCartItemView, name='add_to_cart_item'),
    path('cart/add/service/<int:pk>/', CartViews.addToCartService, name='add_to_cart_service'),
    path('cart/remove/item/<int:pk>/', CartViews.removeFromCartItem, name='remove_from_cart_item'),
    path('cart/remove/service/<int:pk>/', CartViews.removeFromCartService, name='remove_from_cart_service'),
    path('checkout/', CartViews.checkoutView, name='checkout'),

    path('register/', AccountViews.registerView, name='register'),
    path('login/', AccountViews.loginView, name='login'),
    path('logout/', AccountViews.logoutView, name='logout'),
    path('profile/', AccountViews.profileView, name='profile'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        path(
            f"{settings.MEDIA_URL.strip('/')}/<path:path>", 
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]