from django.shortcuts import render, redirect
from usersite.models import User, Product, Category
from django.http import JsonResponse

def page1_view(request, user_id):
    singleUser =User.objects.get(id=user_id)
    context = {
        'singleUser':singleUser
    }
    return render(request, 'Page1.html',context)

def alluser(request):
    allUsers =User.objects.all()
    context = {
        'allUsers':allUsers
    }
    return render(request, 'alluser.html',context)

def login_view(request):
    return render(request, 'login.html')

def registration_view(request):
    return render(request, 'registration.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        is_active = request.POST.get('is_active') == 'on'
        exact_time = request.POST.get('exact_time')

        if User.objects.filter(Email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already taken.'})

        user = User(
            Name=name,
            Email=email,
            Age=age,
            Phone=phone,
            Note=note,
            IsActive=is_active,
            Exact_Time=exact_time
        )
        user.save()
        return redirect('alluserdetail')  
    #JsonResponse({'success': True, 'message': 'User registered successfully.'})

    return render(request, 'registration.html')

def addproduct_view(request):
    allCategory =Category.objects.all()
    context = {
        'allCategory':allCategory
    }
    if request.method == 'POST':
        productname = request.POST.get('Product_Name')
        description = request.POST.get('Description')
        price = request.POST.get('Price')
        stock = request.POST.get('Stock')
        category = request.POST.get('Category')
    
        product = Product(
        Product_Name = productname,
        Description = description,
        Price = price,
        Stock = stock,
        Category = category

        
    )
        product.save()
    return render(request, 'add_product.html', context)


