from modeltranslation.translator import register, TranslationOptions

from posts.models import AuthorModel, PostTagModel, PostModel


@register(AuthorModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PostTagModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
