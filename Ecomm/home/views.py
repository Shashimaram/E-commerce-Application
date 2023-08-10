from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products
# Create your views here.


def index(request):
    # context = {'products': Products.objects.all()}
    return render(request, 'home/index.html',context={'products': Products.objects.all()})