from django.db import models
from quotation_project.users.models import User


class Category(models.Model):
    category_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Category'
    )

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Product Name'
    )
    category = models.ForeignKey('Category',
        verbose_name='Category',
        on_delete=models.CASCADE
    )
    uom = models.CharField(
        max_length=200,
        verbose_name='UOM'
    )
    created_by = models.ForeignKey(User,
        verbose_name='Created By',
    )

    def __str__(self):
        return self.product_name
