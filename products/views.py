from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from quotation_project.users.models import User
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView, ModelFormMixin):
	model = Product
	form_class = ProductForm
	template_name = 'products/product_list.html'

	def get(self, request, *args, **kwargs):
		self.object = None
		self.form = self.get_form(self.form_class)

		return ListView.get(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		self.form = self.get_form(self.form_class)

		if self.form.is_valid():
			self.object = self.form.save(commit=False)
			self.object.created_by = request.user
			self.object.save()
			self.form = self.get_form(self.form_class)

			return HttpResponseRedirect('/products')

		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)

		context['products'] = Product.objects.all()
		context['form'] = self.form
		context['errorlist'] = self.form.errors

		return context
