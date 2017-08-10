from django.db import models
from django.utils import timezone
from datetime import datetime
from quotation_project.users.models import User

# Create your models here.
class Quote(models.Model):
    customer = models.ForeignKey(
        'customers.Customer',
        verbose_name='Customer Details',
    )
    billing_address = models.ForeignKey(
        'customers.Billing_Details',
        verbose_name='Billing Address',
    )
    shipping_address = models.ForeignKey(
        'customers.Shipping_Details',
        verbose_name='Shipping Address',
    )
    QUOTE_CHOICES = (
        ('T1','Template 1: GST Excluded, Quantity Not Required, Total Not Required'),
        ('T2','Template 2: GST Included, Quantity Not Required, Total Not Required'),
        ('T3','Template 3: GST Excluded, Quantity Required, Total Shown'),
        ('T4','Template 4: GST Included, Quantity Required, Total Shown'),
    )
    quote_type = models.CharField(
        max_length=2,
        choices=QUOTE_CHOICES,
        default='T1',
    )
    quote_subtotal = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Subtotal',
    )
    quote_total = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Total',
    )
    quote_gst = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='GST',
    )
    created_by = models.ForeignKey(
        User,
        verbose_name='Created By',
    )
    created_date = models.DateTimeField(
        default=datetime.now,
        verbose_name='Date of Creation',
    )
    confirmation_status = models.BooleanField(
        default=False,
        verbose_name='Confirmation Status',
    )
