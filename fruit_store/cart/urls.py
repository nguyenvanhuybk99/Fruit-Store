from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^add_to_cart/(?P<pk>[0-9]+)$',
        views.add_to_cart,
        name='add_to_cart'
    ),
    url(
        r'^cart',
        views.cart,
        name='cart'
    ),
    url(
        r'^update_cart/(?P<pk>[0-9]+)$',
        views.update_cart,
        name='update_cart'
    ),

]