from django import forms

from posts.models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        exclude = ['created_at', 'post']
        model = CommentModel
