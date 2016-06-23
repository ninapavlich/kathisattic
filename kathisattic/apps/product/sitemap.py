from django.conf import settings
from django.contrib.sitemaps import Sitemap

from carbon.atoms.sitemap.content import SEOSitemap

from .models import Product,ProductTag

class ProductSitemap(SEOSitemap):    
    model = Product

class ProductTagSitemap(SEOSitemap):
  model = ProductTag