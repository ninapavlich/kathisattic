from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageTagView as BasePageTagView
from carbon.compounds.page.views import PageBlockView as BasePageBlockView

from carbon.atoms.views.abstract import *
from carbon.atoms.views.content import *

from .models import *
from .forms import ProductCreateForm
from kathisattic.apps.media.models import Image


class ProductCreateView(ObjectTemplateResponseMixin, CreateView):
    model = Product
    success_message = "%(name)s was created successfully"
    form_class = ProductCreateForm


    def get_template_names(self):
        return ['product-add']

  
    def form_valid(self, form):
        img = Image(image=form.cleaned_data['raw_image'])
        img.save()
        form.instance.image = img
        return super(ProductCreateView, self).form_valid(form)



class ProductDetail(BasePageBlockView, BasePageDetail):

    model = Product


    def get_template_names(self):
        return ['product-detail']

    def get_template(self):
        return self.object.template



class ProductListView(ObjectTemplateResponseMixin, ListView):
    model = Product    

    def get_template_names(self):
        return ['product-list']

    def get_queryset(self):
        tag_filter = self.kwargs['tag']
        if tag_filter:
            try:
                tag = ProductTag.object.get(slug=tag_filter)
                return Product.objects.filter(sale_status=Product.FOR_SALE).filter(tags__in=[tag])
            except:
                return None

        else:
            return Product.objects.filter(sale_status=Product.FOR_SALE)


class ProductTagView(BasePageTagView):

    model = ProductTag
