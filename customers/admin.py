from django.contrib import admin
from .models import Customer, Billing_Details, Shipping_Details
# Register your models here.
admin.site.register(Customer)
admin.site.register(Billing_Details)
admin.site.register(Shipping_Details)
