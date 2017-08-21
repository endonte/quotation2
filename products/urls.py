from django.conf.urls import url
from .views import grid_handler, grid_config

urlpatterns = [
    url(r'^productgrid/$', grid_handler, name='grid_handler'),
	url(r'^productgrid/cfg/$', grid_config, name='grid_config'),
]
