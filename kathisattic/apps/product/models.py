from django.db import models
from django.conf import settings

from carbon.atoms.models.abstract import VersionableAtom, OrderedItemAtom, TitleAtom
from carbon.compounds.page.models import Page as BasePage
from carbon.compounds.page.models import PageTag as BasePageTag
from carbon.compounds.page.models import PageContentBlock as BasePageContentBlock
from carbon.compounds.media.models import Image as BaseImage

from imagekit import ImageSpec
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill, ResizeToFit

from kathisattic.apps.media.models import Image


    
class Product(BasePage):
    default_template = 'product_base'

    tags = models.ManyToManyField('product.ProductSlide', blank=True, related_name='%(app_label)s_%(class)s_tags')

    @property
    def slides(self):
        return ProductSlide.objects.filter(parent=self).order_by('order').select_related('slide_image')

class ProductTag(BasePageTag):  
    default_template = 'product_tag'


class ProductSlide(VersionableAtom, OrderedItemAtom):
    
    parent = models.ForeignKey('product.Product')

    slide_image = models.ForeignKey('media.Image', null=True, blank=True)

    class Meta:
        ordering = ['order']
