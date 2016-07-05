# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default=b'good', max_length=255, null=True, choices=[(b'new', b'New'), (b'like-new', b'Like New'), (b'excellent', b'Excellent'), (b'good', b'Good'), (b'fair', b'Fair'), (b'salvage', b'Salvage')]),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(max_length=255, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.CharField(max_length=255, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=255, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(max_length=255, unique=True, null=True),
        ),
    ]
