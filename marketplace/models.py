from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    """Product categories for the marketplace"""
    
    CATEGORY_CHOICES = (
        ('aquaculture', 'Aquaculture'),
        ('seafoods', 'Seafoods'),
        ('agro_processed', 'Agro-Processed'),
        ('courses', 'Courses Offered'),
        ('tools_rent', 'Tools for Rent'),
        ('jobs', 'Jobs in Agro'),
    )
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class name")
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'display_name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.display_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.display_name


class Listing(models.Model):
    """Main listing/product model"""
    
    MALAYSIAN_STATES = (
        ('johor', 'Johor'),
        ('kedah', 'Kedah'),
        ('kelantan', 'Kelantan'),
        ('melaka', 'Melaka'),
        ('negeri_sembilan', 'Negeri Sembilan'),
        ('pahang', 'Pahang'),
        ('penang', 'Penang'),
        ('perak', 'Perak'),
        ('perlis', 'Perlis'),
        ('sabah', 'Sabah'),
        ('sarawak', 'Sarawak'),
        ('selangor', 'Selangor'),
        ('terengganu', 'Terengganu'),
        ('kuala_lumpur', 'Kuala Lumpur'),
        ('labuan', 'Labuan'),
        ('putrajaya', 'Putrajaya'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    
    # Location
    state = models.CharField(max_length=50, choices=MALAYSIAN_STATES)
    district = models.CharField(max_length=100)
    
    # Images
    image1 = models.ImageField(upload_to='listings/')
    image2 = models.ImageField(upload_to='listings/', blank=True, null=True)
    image3 = models.ImageField(upload_to='listings/', blank=True, null=True)
    image4 = models.ImageField(upload_to='listings/', blank=True, null=True)
    
    # Availability
    available_months = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="Comma-separated month numbers (1-12) or 'always' for year-round availability"
    )
    
    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['category', '-created_at']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_available_months_display(self):
        """Return a formatted string of available months"""
        if not self.available_months:
            return "Not specified"
        
        if self.available_months.lower() == 'always':
            return "Sentiasa Ada (Year-round)"
        
        month_names = {
            '1': 'Jan', '2': 'Feb', '3': 'Mac', '4': 'Apr', 
            '5': 'Mei', '6': 'Jun', '7': 'Jul', '8': 'Ogos',
            '9': 'Sep', '10': 'Okt', '11': 'Nov', '12': 'Dis'
        }
        
        months = self.available_months.split(',')
        month_list = [month_names.get(m.strip(), m.strip()) for m in months if m.strip()]
        return ', '.join(month_list)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('listing_detail', kwargs={'slug': self.slug})
