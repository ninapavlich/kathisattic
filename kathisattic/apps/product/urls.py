from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',
    url(r'^(?P<path>[-_\/\w]*)$', ProductDetail.as_view(), name="product_detail"),
)