from django.shortcuts import render
from .models import Products

from django.http import HttpResponse

# Create your views here.


def get_products(request, slug):

  try:
    product = Products.objects.get(slug=slug) 
  
#   except Products.DoesNotExist:
#     raise Http404("Product does not exist")

  except:
    # log exception
    raise Exception("Something went wrong")
  
  return render(request, 'product/product.html', context={'products': product})


def sampleView(request):
    return HttpResponse("You are  in products ")