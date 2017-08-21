from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from .models import Customer, Billing_Details, Shipping_Details
from .forms import CustomerForm

# Create your views here.

class CustomerListView(ListView, ModelFormMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_list.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/customers')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerListView, self).get_context_data(*args, **kwargs)

        context['customers'] = Customer.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context
