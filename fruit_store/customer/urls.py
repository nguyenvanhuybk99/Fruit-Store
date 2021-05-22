from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^order/(?P<pk>[0-9]+)$',
        views.get_order_detail,
        name='get_order_detail'
    ),
    url(
        r'^order',
        views.get_order_list,
        name='get_order_list'
    ),
    url(
        r'^register',
        views.register,
        name='register'
    ),
    url(
        r'^place_order',
        views.place_order,
        name='order'
    ),
]