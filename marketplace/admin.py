from django.contrib import admin
from .models import Category, Listing

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('display_name', 'description')
    prepopulated_fields = {'slug': ('display_name',)}

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'category', 'price', 'state', 'is_active', 'created_at')
    list_filter = ('category', 'state', 'is_active', 'is_featured')
    search_fields = ('title', 'description', 'seller__username')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
