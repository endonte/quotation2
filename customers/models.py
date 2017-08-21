from django.db import models
from quotation_project.users.models import User

class Customer(models.Model):
    contact_name = models.CharField(
        verbose_name='Contact Name',
        max_length=50,
        help_text='Put Contact Name Here, Do not put business name',
    )
    contact_number = models.IntegerField(
        verbose_name='Contact Number',
        help_text='Put 8 digit Singapore Number',
    )
    contact_email = models.EmailField(
        verbose_name='Contact Email',
    )
    company_name = models.CharField(
        verbose_name='Company Name',
        max_length=75,
        help_text='Business Trading Name',
        null=True,
        blank=True,
    )
    company_reg_no = models.CharField(
        verbose_name='Company Registration Number',
        max_length=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.company_name:
            return self.company_name
        return self.contact

class Billing_Details(models.Model):
    customer_id = models.OneToOneField(Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    billing_address_line1 = models.CharField(
        max_length=75,
        verbose_name='Block Number and Street Name',
    )
    billing_address_line2 = models.CharField(
        max_length=75,
        verbose_name='Unit Number and Building Name',
    )
    billing_postal = models.IntegerField(
        verbose_name='Billing Postal Code',
    )

class Shipping_Details(models.Model):
    customer_id = models.ForeignKey('Customer',
        on_delete=models.CASCADE,
    )
    shipping_address_line1 = models.CharField(
        max_length=75,
        verbose_name='Block Number and Street Name',
    )
    shipping_address_line2 = models.CharField(
        max_length=75,
        verbose_name='Unit Number and Building Name',
    )
    shipping_postal = models.IntegerField(
        verbose_name='Shipping Postal Code',
    )
