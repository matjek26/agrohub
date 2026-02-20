from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from marketplace.models import Listing

User = get_user_model()

class Command(BaseCommand):
    help = 'One-time setup: creates admin and sample data if needed'

    def handle(self, *args, **kwargs):
        # Check if setup already done
        if User.objects.filter(email='admin@test.com').exists() and Listing.objects.count() > 0:
            self.stdout.write(self.style.SUCCESS('✅ Setup already complete!'))
            return
        
        self.stdout.write('🚀 Running first-time setup...')
        
        # Create admin
        if not User.objects.filter(email='admin@test.com').exists():
            self.stdout.write('Creating admin...')
            from users.management.commands.force_admin import Command as ForceAdminCommand
            ForceAdminCommand().handle()
        
        # Load sample data
        if Listing.objects.count() == 0:
            self.stdout.write('Loading sample data...')
            from marketplace.management.commands.populate_sample_data import Command as PopulateCommand
            PopulateCommand().handle()
        
        self.stdout.write(self.style.SUCCESS('✅ Setup complete!'))
