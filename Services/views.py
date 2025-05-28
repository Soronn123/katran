from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from Services.models import ItemModel, ServiceModel, TypeModel

def productsView(request):
    types = TypeModel.objects.all()
    
    products_list = ItemModel.objects.all().order_by('-dateCreated')
    
    paginator = Paginator(products_list, 8)  # 8 товаров на странице
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'types': types,
    }

    return render(request, 'Services/productsList.html', context)

def servicesView(request):
    types = TypeModel.objects.all()
    services = ServiceModel.objects.all()

    context = {
        'services': services,
        'types': types,
    }

    return render(request, 'Services/servicesList.html', context)


def itemDetailView(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    similar_items = ItemModel.objects.filter(typeId=item.typeId).exclude(pk=pk)[:4]
    
    context = {
        'item': item,
        'similar_items': similar_items,
    }
    return render(request, 'Services/itemDetail.html', context)

def serviceDetailView(request, pk):
    service = get_object_or_404(ServiceModel, pk=pk)
    other_services = ServiceModel.objects.exclude(pk=pk)[:3]
    
    context = {
        'service': service,
        'other_services': other_services,
    }
    return render(request, 'Services/serviceDetail.html', context)

