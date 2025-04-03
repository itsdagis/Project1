from django.shortcuts import render

def page1_view(request):
    return render(request, 'Page1.html')

def login_view(request):
    return render(request, 'login.html')

def registration_view(request):
    return render(request, 'registration.html')
