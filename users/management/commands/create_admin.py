from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser with known credentials'

    def handle(self, *args, **kwargs):
        email = 'admin@agrohub.com'
        username = 'admin'
        password = 'admin123'
        
        # Delete if exists
        if User.objects.filter(email=email).exists():
            User.objects.filter(email=email).delete()
            self.stdout.write('Deleted existing admin user')
        
        # Create new superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            full_name='Admin User'
        )
        
        self.stdout.write(self.style.SUCCESS('✅ Superuser created successfully!'))
        self.stdout.write('')
        self.stdout.write('=== LOGIN CREDENTIALS ===')
        self.stdout.write(f'Email: {email}')
        self.stdout.write(f'Password: {password}')
        self.stdout.write('')
        self.stdout.write('Login at: /admin')
