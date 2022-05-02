from django.urls import path

from pages.views import ContactCreateView, AboutTemplateView, HomeTemplateView, WishlistListView, add_to_wishlist

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
    path('', HomeTemplateView.as_view(), name='home'),
]
