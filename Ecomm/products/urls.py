from django.urls import path
from products.views import get_products, sampleView

urlpatterns = [
    path('<slug>/',get_products,name='get_products'),
    path('',sampleView,name='sample'),
]