from django.conf.urls import patterns, url, include
from django.contrib.admin.views.decorators import staff_member_required

from .views import *

urlpatterns = patterns('',
    url(r'^products/add/$', staff_member_required(ProductCreateView.as_view()),  name='product_add_view' ), 
    url(r'^products/(?P<path>[\w-]*)/$', ProductDetail.as_view(), name="product_detail"),
)