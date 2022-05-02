from django.urls import include, path
from auth.views import password_change

urlpatterns = [
    path('password/change/done/', password_change),
    path('', include('registration.backends.default.urls')),
]
