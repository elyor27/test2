from math import ceil

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min, Max
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, BrandModel, ProductTagModel, ColorModel, SizeModel


class ProductListView(ListView):
    template_name = 'products.html'
    paginate_by = 9

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category__id=cat)

        if brand:
            qs = qs.filter(brand__id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if size:
            qs = qs.filter(sizes__id=size)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['sizes'] = SizeModel.objects.all()

        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.object.category.products.exclude(pk=self.object.pk)[:4]
        return context


class CartListView(ListView):
    template_name = 'cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.objects.filter(
            pk__in=cart
        )


def add_to_cart(request, pk):
    cart = request.session.get('cart')

    if not cart:
        cart = []

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))
