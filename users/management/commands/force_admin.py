from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Force create/update admin user with known credentials'

    def handle(self, *args, **kwargs):
        email = 'admin@test.com'
        password = 'Test123456!'
        
        # Try to get or create user
        try:
            user = User.objects.get(email=email)
            self.stdout.write(f'Found existing user: {email}')
        except User.DoesNotExist:
            user = User.objects.create(
                username='testadmin',
                email=email,
                full_name='Test Admin'
            )
            self.stdout.write('Created new user')
        
        # Force set everything
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        
        self.stdout.write(self.style.SUCCESS('✅ Admin user ready!'))
        self.stdout.write('')
        self.stdout.write('=== LOGIN CREDENTIALS ===')
        self.stdout.write(f'Email: {email}')
        self.stdout.write(f'Password: {password}')
        self.stdout.write(f'Is Staff: {user.is_staff}')
        self.stdout.write(f'Is Superuser: {user.is_superuser}')
        self.stdout.write(f'Is Active: {user.is_active}')
