# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160628_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='key',
            field=models.CharField(max_length=255, unique=True, null=True),
        ),
    ]
