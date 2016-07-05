from django.db.models import Q
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
    tag = None
    search_filter = None

    def get_template_names(self):
        return ['product-list']

    def get_queryset(self):
        tag_filter = self.request.GET.get('tag', None)
        search_filter = self.request.GET.get('q', None)
        products = Product.objects.filter(sale_status=Product.FOR_SALE)

        if tag_filter:
            try:
                tag = ProductTag.objects.get(slug=tag_filter)
                self.tag = tag
                return products.filter(tags__in=[tag])
            except:
                return None

        elif search_filter:
            self.search_filter = search_filter
            return products.filter(
                Q(content__icontains=search_filter)|Q(title__icontains=search_filter)|Q(key__icontains=search_filter)|Q(synopsis__icontains=search_filter)
            )

        else:
            return products

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        context['search_filter'] = self.search_filter
        return context


class ProductTagView(BasePageTagView):

    model = ProductTag
