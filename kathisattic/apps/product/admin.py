from django.contrib import admin
from django.core.urlresolvers import reverse

from carbon.atoms.admin.content import BaseVersionableAdmin
from carbon.compounds.page.admin import PageAdmin as BasePageAdmin
from carbon.compounds.page.admin import PageTagAdmin as BasePageTagAdmin
from carbon.compounds.page.admin import PageContentBlockInline as BasePageContentBlockInline
from carbon.atoms.admin.taxonomy import BaseCategoryAdmin

from django_unsaved_changes.admin import UnsavedChangesAdmin

from django_inline_wrestler.admin import TabularInlineOrderable

from .models import *

class ProductSlideInlineAdmin(TabularInlineOrderable):
    
    model = ProductSlide
    extra = 0

    autocomplete_lookup_fields = {
        'fk': ('slide_image',),
    }
    raw_id_fields = ( 'slide_image',)

    def preview(self, obj):
        if obj.slide_image:
            try:
                return "<img src='%s' alt='%s preview'/>"%(obj.slide_image.thumbnail.url, obj.slide_image.title)
            except:
                return ""
        return ''
    preview.allow_tags = True

    def edit_image(self, obj):
        style="style='width:278px;display:block;'"
        if obj.slide_image.pk:            
            try:
                object_type = type(obj.slide_image).__name__
                url = reverse('admin:%s_%s_change' %(obj.slide_image._meta.app_label,  obj.slide_image._meta.model_name),  args=[obj.slide_image.id] )
                return '<a href="%s" %s>Edit Image &gt;</a>'%(url, style)
            except:
                return '<span %s>&nbsp;</span>'%(style)
        return '<span %s>&nbsp;</span>'%(style)
    edit_image.allow_tags = True


    readonly_fields = ('preview','edit_image')
    fields = (
        'order',
        'slide_image',
        'preview',
        'edit_image'
    )



class ProductAdmin(BasePageAdmin, UnsavedChangesAdmin):
    inlines = [ProductSlideInlineAdmin]

    #related_blogposts

    core_fields_list = list(BasePageAdmin.core_fields)
    core_fields_list.insert(5, 'tags')
    core_fields_list.insert(5, ('suggested_price', 'sale_price'))
    core_fields_list.insert(5, 'sale_status')
    core_fields = tuple(core_fields_list)



    autocomplete_lookup_fields = BasePageAdmin.autocomplete_lookup_fields
    m2m_fields_list = list(autocomplete_lookup_fields['m2m'])
    m2m_fields_list.insert(0, 'tags')
    autocomplete_lookup_fields['m2m'] = tuple(m2m_fields_list)
    
    raw_id_fields = BasePageAdmin.raw_id_fields
    raw_id_fields_list = list(raw_id_fields)
    raw_id_fields_list.insert(0, 'tags')
    raw_id_fields = tuple(raw_id_fields_list)

    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        
        ("Path", {
            'fields': BasePageAdmin.path_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Publication", {
            'fields': BasePageAdmin.publication_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Search Engine Optimization", {
            'fields': BasePageAdmin.seo_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Social Integration", {
            'fields': BasePageAdmin.social_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Meta", {
            'fields': BasePageAdmin.meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )

class ProductTagAdmin(BaseCategoryAdmin, UnsavedChangesAdmin):
    pass





admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
