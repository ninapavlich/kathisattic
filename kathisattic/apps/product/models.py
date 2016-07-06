import uuid

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from carbon.atoms.models.abstract import VersionableAtom, OrderedItemAtom, TitleAtom
from carbon.atoms.models.content import HierarchicalAtom
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
    DRAFT = 'draft'
    FOR_SALE = 'for-sale'
    SOLD = 'sold'
    DONATED = 'donated'
    SALE_STATUS_OPTIONS = (
        (DRAFT, 'Draft'),
        (FOR_SALE, 'For Sale'),
        (SOLD, 'Sold'),
        (DONATED, 'Donated'),
    )

    NEW = 'new'
    LIKE_NEW = 'like-new'
    EXCELLENT = 'excellent'
    GOOD = 'good'
    FAIR = 'fair'
    SALVAGE = 'salvage'
    CONDITION_OPTIONS = (
        (NEW, 'New'),
        (LIKE_NEW, 'Like New'),
        (EXCELLENT, 'Excellent'),
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
        (SALVAGE, 'Salvage'),
    )

    

    #suggested_price
    #sale_price
    #sale_status - draft, for sale, sold, donated
    #ID - charfield 

    tags = models.ManyToManyField('product.ProductTag', blank=True, related_name='%(app_label)s_%(class)s_tags')
    suggested_price = models.FloatField(null=True, blank=True, default=None)
    sale_price = models.FloatField(null=True, blank=True, default=None)
    sale_status = models.CharField(
        max_length=255,
        choices=SALE_STATUS_OPTIONS,
        default=DRAFT,
        null=True
    )
    key = models.CharField(max_length=255,null=True, unique=True)

    length = models.CharField(max_length=255,null=True, blank=True)
    width = models.CharField(max_length=255,null=True, blank=True)
    height = models.CharField(max_length=255,null=True, blank=True)
    weight = models.CharField(max_length=255,null=True, blank=True)
    condition = models.CharField(
        max_length=255,
        choices=CONDITION_OPTIONS,
        default=GOOD,
        null=True
    )
    related_products = models.ManyToManyField('self', blank=True, related_name='%(app_label)s_%(class)s_related_products')

    def get_absolute_url(self):
       return reverse('product_detail',  args=[self.slug] )

    @property
    def slides(self):
        return ProductSlide.objects.filter(parent=self).order_by('order').select_related('slide_image')

    def get_price(self):
        if self.suggested_price:
            return '$%s'%(self.suggested_price)
        return ''

    def get_page_content_blocks(self):
        return []

    def save(self, *args, **kwargs):
        
        if not self.key:
            self.key = str(uuid.uuid4())[:5]

        #always be published, using sale_status to manage status.
        if not self.pk:
            self.publication_status = 100

        super(Product, self).save(*args, **kwargs)
         

class ProductTag(BasePageTag, HierarchicalAtom):  
    default_template = 'product_tag'

    def get_absolute_url(self):
       return "%s?tag=%s"%(reverse('product_list_view'), self.slug)

    def get_product_count(self):
       return Product.objects.filter(sale_status=Product.FOR_SALE).filter(tags__in=[self]).count()


class ProductSlide(VersionableAtom, OrderedItemAtom):
    
    parent = models.ForeignKey('product.Product')

    slide_image = models.ForeignKey('media.Image', null=True, blank=True)


    class Meta:
        ordering = ['order']
