from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    newest_product = Product.objects.order_by('price')
    context = {'newest_product': newest_product}
    return render(request, 'dashboard/index.html', context)
