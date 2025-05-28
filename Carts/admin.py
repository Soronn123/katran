from django.contrib import admin

from Carts.models import CartItemModel, CartServiceModel, PaymentModel

admin.site.register(CartItemModel)
admin.site.register(CartServiceModel)
admin.site.register(PaymentModel)
