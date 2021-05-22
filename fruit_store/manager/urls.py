from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^product/(?P<pk>[0-9]+)$',
        views.get_delete_update_product,
        name='ad_get_delete_update_product'
    ),
    url(
        r'^product',
        views.get_post_product,
        name='ad_get_post_product'
    ),
    url(
        r'^customer',
        views.get_all_customer,
        name='ad_get_all_customer'
    ),
    url(
        r'^order/(?P<pk>[0-9]+)$',
        views.get_order_detail,
        name='ad_get_order_detail'
    ),
    url(
        r'^order',
        views.get_order_list,
        name='ad_get_order_list'
    ),
    
]