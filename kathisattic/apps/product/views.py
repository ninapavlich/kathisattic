from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageTagView as BasePageTagView
from carbon.compounds.page.views import PageBlockView as BasePageBlockView

from .models import *


class ProductDetail(BasePageBlockView, BasePageDetail):

    model = Product

class ProductTagView(BasePageTagView):

    model = ProductTag
