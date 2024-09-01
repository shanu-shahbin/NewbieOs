from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to auth_login
from .models import Customer

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using email instead of username
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.username == 'admin':
                return render(request, 'dashboard.html')
            else:
                auth_login(request, user)  # Use auth_login instead of login
                return redirect('index')
        else:
            return render(request, 'login.html', {'error': "Invalid email or password"})

    return render(request, 'login.html')



@csrf_protect
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Validate phone number
        if not phone_number or len(phone_number) != 10:
            error_message = "Enter a correct 10-digit phone number"
            return render(request, 'signup.html', {'error': error_message})

        # Check if email or phone number already exists
        if Customer.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email already exists"})
        if Customer.objects.filter(number=phone_number).exists():
            return render(request, 'signup.html', {'error': "Phone number already exists"})

        # Create the user without unique username constraint
        user = User.objects.create_user(
            username=name,  # Username can be non-unique
            email=email,
            password=password,
        )
        user.save()

        # Create the customer profile
        customer = Customer.objects.create(
            user=user,
            name=name,
            email=email,
            user_type=user_type,
            number=phone_number
        )
        customer.save()

        # Redirect to the index page after successful signup
        return redirect('index')  # Use redirect to prevent form resubmission

    return render(request, 'signup.html')
