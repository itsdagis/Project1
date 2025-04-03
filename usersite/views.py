from django.shortcuts import render

def page3_view(request):
    return render(request, 'Page3.html')

def userhome_view(request):
    return render(request, 'user_home.html')

def userorder_view(request):
    return render(request, 'order_page.html')
