from django.urls import reverse_lazy
from jqgrid import JqGrid
from .models import Product

class ProductGrid(JqGrid):
    model = Product
    fields = ['id', 'product_name', 'category', 'uom']
    url = reverse_lazy('grid_handler')
    caption = 'Product Grid'
    colmodel_overrides = {
        'id': { 'editable':False, 'width': 10 },
    }
