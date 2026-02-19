from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from marketplace.models import Category, Listing
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to populate sample data...'))
        
        # Create categories if they don't exist
        categories_data = [
            {'name': 'aquaculture', 'display_name': 'Aquaculture', 'description': 'Fish farming and aquatic products', 'order': 1},
            {'name': 'seafoods', 'display_name': 'Seafoods', 'description': 'Fresh seafood products', 'order': 2},
            {'name': 'agro_processed', 'display_name': 'Agro-Processed', 'description': 'Processed agricultural goods', 'order': 3},
            {'name': 'courses', 'display_name': 'Courses Offered', 'description': 'Agricultural training and courses', 'order': 4},
            {'name': 'tools_rent', 'display_name': 'Tools for Rent', 'description': 'Agricultural equipment rental', 'order': 5},
            {'name': 'jobs', 'display_name': 'Jobs in Agro', 'description': 'Career opportunities in agriculture', 'order': 6},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.display_name}'))
            else:
                self.stdout.write(f'Category already exists: {category.display_name}')
        
        # Create a sample seller if doesn't exist
        seller, created = User.objects.get_or_create(
            email='seller@agrohub.my',
            defaults={
                'username': 'demo_seller',
                'user_type': 'seller',
                'first_name': 'Ahmad',
                'last_name': 'Farmer',
            }
        )
        if created:
            seller.set_password('demo123')
            seller.save()
            seller.profile.company_name = 'Ahmad Agro Farm'
            seller.profile.is_verified = True
            seller.profile.state = 'Johor'
            seller.profile.save()
            self.stdout.write(self.style.SUCCESS('Created demo seller account'))
        
        # Sample listings data
        sample_listings = [
            {
                'title': 'Fresh Tilapia Fish - Grade A Quality',
                'description': 'Premium quality tilapia fish, freshly harvested. Suitable for restaurants and home cooking. Minimum order 5kg. Free delivery for orders above RM100.',
                'price': Decimal('15.00'),
                'category': 'aquaculture',
                'state': 'johor',
                'district': 'Johor Bahru',
                'is_featured': True,
            },
            {
                'title': 'Organic Prawns - Live & Fresh',
                'description': 'Organically farmed prawns, no antibiotics. Harvested daily. Perfect for seafood restaurants. Available in bulk orders.',
                'price': Decimal('45.00'),
                'category': 'seafoods',
                'state': 'selangor',
                'district': 'Klang',
                'is_featured': True,
            },
            {
                'title': 'Rice Milling Machine for Rent',
                'description': 'Modern rice milling machine available for rent. Capacity: 1 ton/hour. Perfect for medium-scale farmers. Daily and monthly rates available.',
                'price': Decimal('200.00'),
                'category': 'tools_rent',
                'state': 'kedah',
                'district': 'Sungai Petani',
            },
            {
                'title': 'MyGAP Certification Training Course',
                'description': '3-day comprehensive training on Malaysian Good Agricultural Practices. Certificate provided. Expert instructors with 10+ years experience.',
                'price': Decimal('500.00'),
                'category': 'courses',
                'state': 'kuala_lumpur',
                'district': 'Kuala Lumpur',
            },
            {
                'title': 'Premium Durian Paste - Musang King',
                'description': 'Pure Musang King durian paste, no preservatives. Perfect for baking and desserts. Vacuum sealed packaging. Halal certified.',
                'price': Decimal('35.00'),
                'category': 'agro_processed',
                'state': 'pahang',
                'district': 'Raub',
                'is_featured': True,
            },
            {
                'title': 'Farm Manager Position - Urgent Hiring',
                'description': 'Seeking experienced farm manager for 50-acre oil palm plantation. Requirements: 5 years experience, valid driving license. Competitive salary + accommodation.',
                'price': Decimal('4500.00'),
                'category': 'jobs',
                'state': 'sabah',
                'district': 'Lahad Datu',
            },
        ]
        
        created_count = 0
        for listing_data in sample_listings:
            category_name = listing_data.pop('category')
            category = Category.objects.get(name=category_name)
            
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults={
                    **listing_data,
                    'category': category,
                    'seller': seller,
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Sample data population complete!'))
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} new listings'))
        self.stdout.write(self.style.WARNING('\nDemo Account:'))
        self.stdout.write(f'  Email: seller@agrohub.my')
        self.stdout.write(f'  Password: demo123')
