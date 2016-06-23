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

from ..models import Page, AvailableDay


@register.assignment_tag()
def get_unpublished_childred_by_slug(slug):
   
    try:
        item = Page.objects.get(slug=slug)
        return item.get_children(False)
    except:
        return []


@register.assignment_tag()
def get_random_quote():
   
    try:
        item = Page.objects.get(slug='quotes')
        children = item.get_children(False)
        return random.choice(children)
    except:
        return None



@register.assignment_tag()
def get_available_dates():
   
    return AvailableDay.objects.all()

@register.assignment_tag()
def get_next_available_date():
    # try:
        return AvailableDay.objects.filter(day__gt=datetime.datetime.today())[0]
    # except:
    #     return None