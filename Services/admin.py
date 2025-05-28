from django.contrib import admin

from Services.models import ItemModel, TypeModel, ServiceModel, IconModel

admin.site.register(ItemModel)
admin.site.register(TypeModel)
admin.site.register(ServiceModel)
admin.site.register(IconModel)