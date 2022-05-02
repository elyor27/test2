from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', HomepageTemplateView.as_view(), name='home'),
]

