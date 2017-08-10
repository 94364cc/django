from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
admin.autodiscover()

urlpatterns = patterns('',

    (r'product/list/$',product_list),
    (r'product/create/$',create_product),
    (r'product/edit/(?P<id>[^/]+)/$',edit_product),
    (r'product/view/(?P<id>[^/]+)/$',view_product),
    (r'product/update/$',update_product),
    (r'product/delete/(?P<id>[^/]+)$',delete_product),
    (r'product/add/$',add_product),

)
