from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel, ProductImageModel, SizeModel, \
    ColorModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


# class ColorForm(forms.ModelForm):
#     class Meta:
#         model = ColorModel
#         fields = '__all__'
#         widgets = {
#             'code': forms.TextInput(attrs={'type': 'color'}),
#         }


# @admin.register(ColorModel)
# class ColorModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'code', 'created_at']
#     list_filter = ['created_at']
#     search_fields = ['title', 'code']
#     form = ColorForm


class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'category', 'brand', 'price', 'discount', 'short_description', 'created_at']
    search_fields = ['title', 'category__title', 'short_description']
    list_filter = ['category', 'brand', 'tags', 'created_at']
    autocomplete_fields = ['category', 'brand', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price']

    inlines = [ProductImageModelAdmin]

    def change_view(self, request, **kwargs):
        self.exclude = ('wishlist',)
        return super().change_view(request, **kwargs)
