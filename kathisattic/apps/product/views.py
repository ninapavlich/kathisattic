from django.views.generic.edit import CreateView


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

    def get_template(self):
        return self.object.template

  
    def form_valid(self, form):
        print 'form valid? %s'%(form.cleaned_data['raw_image'])
        img = Image(image=form.cleaned_data['raw_image'])
        img.save()
        print 'IMAGE? %s'%(img)
        form.instance.image = img
        # try:
        #     user = User.objects.get(email=form.email)
        # except User.DoesNotExist:
        #     user = User.objects.create_user(form.email, form.email, ''.join([random.choice(string.digits + string.letters) for i in range(0, 10)]))
        #     user.save()
        # form.instance.user = user
        return super(ProductCreateView, self).form_valid(form)



class ProductDetail(BasePageBlockView, BasePageDetail):

    model = Product


    def get_template_names(self):
        return ['product-detail']

    def get_template(self):
        return self.object.template

class ProductTagView(BasePageTagView):

    model = ProductTag
