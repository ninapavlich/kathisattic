import random
import datetime

from django.template import Library
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.exceptions import ImproperlyConfigured
try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model

register = Library()

from ..models import *


@register.assignment_tag()
def get_tags():
    return ProductTag.objects.all()


@register.assignment_tag()
def get_products_for_sale():   
    return Product.objects.filter(sale_status=Product.FOR_SALE)
