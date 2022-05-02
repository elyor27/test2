from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def succes(request, uid):
    email = EmailMessage(
        'subject',
        'body',
        settings.Email_Host[],
    )

    email.fail_silently=False
    email.send()

    project = Contact.objects.get(id=uid)
    context = {'project':project}

    return render(request, 'contact.html', context)



from orders.forms import OrderModelForm
from products.models import ProductModel


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('orders:history')

    def form_valid(self, form):
        products = ProductModel.get_from_cart(self.request)

        form.instance.user = self.request.user
        form.instance.price = products.aggregate(
            Sum('real_price')
        )['real_price__sum']

        order = form.save()

        order.products.set(products)

        self.request.session['cart'] = []

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = ProductModel.get_from_cart(self.request)
        if hasattr(self.request.user, 'profile'):
            context['profile'] = self.request.user.profile

        return context


class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return self.request.user.orders.all()

from django.core.mail import Emailm