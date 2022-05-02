from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView

from pages.forms import ContactModelForm
from posts.models import PostModel
from products.models import ProductModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.order_by('-pk')[:4]
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'
    paginate_by = 9

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))
