from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from main.forms import ContactModelForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from .models import *


class NewsListView(ListView):
    template_name = 'news.html'
    queryset = NewsModel.objects.order_by('-pk')


class StaffListView(ListView):
    template_name = 'staff.html'
    queryset = StaffModel.objects.order_by('-pk')


class GalleryListView(ListView):
    template_name = 'gallery.html'
    paginate_by = 4
    queryset = GalleryModel.objects.order_by('-pk')


class HomepageTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['banners'] = BannerModel.objects.order_by('-pk')
        context['news'] = NewsModel.objects.order_by('-pk')[:3]
        context['gallery'] = GalleryModel.objects.order_by('-pk')[:4]

        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save()
        text = f'Name: {obj.name}\nPhone: {obj.phone}\nMessage: {obj.text}'
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(self.success_url)


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'details.html'
