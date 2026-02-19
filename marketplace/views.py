from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import Listing, Category
import json

def home(request):
    """Homepage view with featured listings"""
    categories = Category.objects.filter(is_active=True)
    featured_listings = Listing.objects.filter(is_active=True, is_featured=True)[:6]
    trending_listings = Listing.objects.filter(is_active=True).order_by('-views_count')[:8]
    
    # Get listing counts by state for map markers
    state_counts = Listing.objects.filter(is_active=True).values('state').annotate(count=Count('id'))
    
    # Convert to dictionary for easier access in template
    state_data = {item['state']: item['count'] for item in state_counts}
    state_data_json = json.dumps(state_data)
    
    context = {
        'categories': categories,
        'featured_listings': featured_listings,
        'trending_listings': trending_listings,
        'state_data': state_data,
        'state_data_json': state_data_json,
    }
    return render(request, 'marketplace/home.html', context)


def listing_detail(request, slug):
    """Listing detail view"""
    listing = get_object_or_404(Listing, slug=slug, is_active=True)
    
    # Increment view count
    listing.views_count += 1
    listing.save(update_fields=['views_count'])
    
    # Get related listings
    related_listings = Listing.objects.filter(
        category=listing.category,
        is_active=True
    ).exclude(id=listing.id)[:4]
    
    context = {
        'listing': listing,
        'related_listings': related_listings,
    }
    return render(request, 'marketplace/listing_detail.html', context)


def search(request):
    """Search listings"""
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    state = request.GET.get('state', '')
    
    listings = Listing.objects.filter(is_active=True)
    
    if query:
        listings = listings.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    if category_slug:
        listings = listings.filter(category__slug=category_slug)
    
    if state:
        listings = listings.filter(state=state)
    
    categories = Category.objects.filter(is_active=True)
    
    context = {
        'listings': listings,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
        'selected_state': state,
    }
    return render(request, 'marketplace/search.html', context)


def category_view(request, slug):
    """View listings by category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    listings = Listing.objects.filter(category=category, is_active=True)
    
    context = {
        'category': category,
        'listings': listings,
    }
    return render(request, 'marketplace/category.html', context)


@login_required
def create_listing(request):
    """Create a new listing"""
    if request.method == 'POST':
        # Handle listing creation
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        state = request.POST.get('state')
        district = request.POST.get('district')
        image1 = request.FILES.get('image1')
        
        # Handle availability months
        always_available = request.POST.get('always_available')
        if always_available:
            available_months = 'always'
        else:
            selected_months = request.POST.getlist('months')
            available_months = ','.join(selected_months) if selected_months else ''
        
        listing = Listing.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id,
            seller=request.user,
            state=state,
            district=district,
            image1=image1,
            available_months=available_months
        )
        
        messages.success(request, 'Listing created successfully!')
        return redirect('listing_detail', slug=listing.slug)
    
    categories = Category.objects.filter(is_active=True)
    context = {'categories': categories}
    return render(request, 'marketplace/create_listing.html', context)
