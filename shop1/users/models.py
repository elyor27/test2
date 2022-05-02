from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    postcode = models.CharField(max_length=30, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
