from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from marketplace.models import Listing

User = get_user_model()

@require_http_methods(["GET"])
def setup_view(request):
    """One-time setup endpoint"""
    output = []
    
    # Check if already set up
    if User.objects.filter(email='admin@test.com').exists() and Listing.objects.count() > 0:
        return HttpResponse("✅ Setup already complete!<br><br>Admin: admin@test.com / Test123456!<br><a href='/admin'>Go to Admin</a> | <a href='/'>Go to Home</a>")
    
    output.append("🚀 Running setup...<br><br>")
    
    # Create admin
    try:
        if not User.objects.filter(email='admin@test.com').exists():
            output.append("Creating admin user...<br>")
            user = User.objects.create_superuser(
                username='testadmin',
                email='admin@test.com',
                password='Test123456!',
                full_name='Admin User'
            )
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.save()
            output.append("✅ Admin created!<br>")
    except Exception as e:
        output.append(f"⚠️ Admin error: {e}<br>")
    
    # Load sample data
    try:
        if Listing.objects.count() == 0:
            output.append("Loading sample data...<br>")
            from django.core.management import call_command
            call_command('populate_sample_data')
            output.append(f"✅ Created {Listing.objects.count()} listings!<br>")
    except Exception as e:
        output.append(f"⚠️ Data error: {e}<br>")
    
    output.append("<br><br>✅ Setup complete!<br><br>")
    output.append("<strong>Admin Login:</strong><br>")
    output.append("Email: admin@test.com<br>")
    output.append("Password: Test123456!<br><br>")
    output.append("<a href='/admin'>Go to Admin Panel</a> | <a href='/'>Go to Homepage</a>")
    
    return HttpResponse(''.join(output))
