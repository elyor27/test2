from django.db import models


class StaffModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff')
    position = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery')
    text = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    description = models.TextField(null=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners')
    text = models.CharField(max_length=512, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
