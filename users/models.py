from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Custom User model with email as primary identifier"""
    
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller/Company'),
    )
    
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True, help_text='Full name as per IC')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    """Extended profile information for users"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # For Buyers
    ic_number = models.CharField(max_length=20, blank=True, null=True, help_text='IC Number without dashes')
    
    # For Sellers/Companies
    company_name = models.CharField(max_length=200, blank=True, null=True)
    business_registration = models.CharField(max_length=100, blank=True, null=True, help_text='SSM/ROC Number')
    
    # Farm/Factory Details (Sellers only)
    farm_picture_1 = models.ImageField(upload_to='farms/', blank=True, null=True)
    farm_picture_2 = models.ImageField(upload_to='farms/', blank=True, null=True)
    farm_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    farm_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Certifications (Sellers only)
    halal_certificate = models.CharField(max_length=100, blank=True, null=True)
    mygap_certificate = models.CharField(max_length=100, blank=True, null=True)
    haccp_certificate = models.CharField(max_length=100, blank=True, null=True)
    other_certificate = models.CharField(max_length=200, blank=True, null=True, help_text='MESTI, etc.')
    
    # Common fields
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    farm_details_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
