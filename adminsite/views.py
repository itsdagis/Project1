from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def page2_view(request):
    return render(request, 'Page2.html')

def home_view(request):
    return render(request, 'Page2.html')

def addproduct_view(request):
    return render(request, 'add_product.html')