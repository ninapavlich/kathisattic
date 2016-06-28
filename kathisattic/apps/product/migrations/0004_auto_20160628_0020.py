# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160627_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='product_product_tags', to='product.ProductTag', blank=True),
        ),
    ]
