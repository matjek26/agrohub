from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('listing/create/', views.create_listing, name='create_listing'),
    path('listing/<slug:slug>/', views.listing_detail, name='listing_detail'),
    path('category/<slug:slug>/', views.category_view, name='category'),
]
