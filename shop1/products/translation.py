from modeltranslation.translator import register, TranslationOptions

from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BrandModel)
class BrandTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductTagModel)
class ProductTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
