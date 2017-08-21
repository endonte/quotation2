from django.shortcuts import render
from django.http import HttpResponse
from .utilities import ProductGrid

# Create your views here.
def grid_handler(request):
	# handles pagination, sorting and searching
	grid = ProductGrid()
	return HttpResponse(grid.get_json(request), content_type="application/json")

def grid_config(request):
    # build a config suitable to pass to jqgrid constructor
    grid = ProductGrid()
    return HttpResponse(grid.get_config(), content_type="application/json")
