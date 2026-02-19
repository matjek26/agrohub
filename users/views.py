from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def register(request):
    """User registration view"""
    if request.method == 'POST':
        # Common fields
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone_number = request.POST.get('phone_number')
        user_type = request.POST.get('user_type', 'buyer')
        
        # Validation
        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return render(request, 'users/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'users/register.html')
        
        # Get user type specific fields
        if user_type == 'buyer':
            full_name = request.POST.get('full_name')
            ic_number = request.POST.get('ic_number')
            username = email.split('@')[0]  # Generate username from email
        else:  # seller
            company_name = request.POST.get('company_name')
            business_registration = request.POST.get('business_registration')
            username = company_name.replace(' ', '_').lower() if company_name else email.split('@')[0]
            full_name = company_name
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                phone_number=phone_number,
                full_name=full_name
            )
            
            # Update profile with additional fields
            if user_type == 'buyer':
                user.profile.ic_number = ic_number
            else:  # seller
                user.profile.company_name = company_name
                user.profile.business_registration = business_registration
            
            user.profile.save()
            
            login(request, user)
            messages.success(request, f'Welcome to AGROHUB, {full_name}!')
            
            # Redirect sellers to farm details page
            if user_type == 'seller':
                return redirect('seller_farm_details')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'users/register.html')
    
    return render(request, 'users/register.html')


def user_login(request):
    """User login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'users/login.html')


def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


@login_required
def profile(request):
    """User profile view"""
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def seller_farm_details(request):
    """Seller farm details setup view"""
    if request.user.user_type != 'seller':
        messages.error(request, 'Only sellers can access this page')
        return redirect('home')
    
    if request.method == 'POST':
        profile = request.user.profile
        
        # Handle farm pictures
        if request.FILES.get('farm_picture_1'):
            profile.farm_picture_1 = request.FILES['farm_picture_1']
        if request.FILES.get('farm_picture_2'):
            profile.farm_picture_2 = request.FILES['farm_picture_2']
        
        # Handle location
        profile.state = request.POST.get('state')
        profile.district = request.POST.get('district')
        profile.farm_latitude = request.POST.get('farm_latitude') or None
        profile.farm_longitude = request.POST.get('farm_longitude') or None
        
        # Handle certifications
        profile.halal_certificate = request.POST.get('halal_certificate')
        profile.mygap_certificate = request.POST.get('mygap_certificate')
        profile.haccp_certificate = request.POST.get('haccp_certificate')
        profile.other_certificate = request.POST.get('other_certificate')
        
        profile.farm_details_completed = True
        profile.save()
        
        messages.success(request, 'Farm details saved successfully!')
        return redirect('profile')
    
    return render(request, 'users/seller_farm_details.html')
