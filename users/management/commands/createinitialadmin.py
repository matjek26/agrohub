from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates an initial admin user if none exists'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@agrohubmy.com',
                password='ChangeThisPassword123!',
                full_name='Admin User'
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully!'))
            self.stdout.write(self.style.WARNING('Username: admin'))
            self.stdout.write(self.style.WARNING('Password: ChangeThisPassword123!'))
            self.stdout.write(self.style.WARNING('PLEASE CHANGE THIS PASSWORD IMMEDIATELY!'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
