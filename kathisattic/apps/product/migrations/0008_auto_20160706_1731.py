# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_related_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
