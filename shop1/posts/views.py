from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import CommentModelForm
from posts.models import PostModel


class PostListView(ListView):
    template_name = 'blog.html'
    paginate_by = 6

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)

        return qs


class PostDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.post = get_object_or_404(PostModel, pk=pk)
        return super().form_valid(form)
