from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^product/(?P<pk>[0-9]+)$',
        views.get,
        name='get_product'
    ),
    url(
        r'^product',
        views.get_all,
        name='get_all_product'
    )
]