# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_producttag_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_status',
            field=models.CharField(default=b'draft', max_length=255, null=True, choices=[(b'draft', b'Draft'), (b'for-sale', b'For Sale'), (b'sold', b'Sold'), (b'donated', b'Donated')]),
        ),
        migrations.AddField(
            model_name='product',
            name='suggested_price',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
    ]
