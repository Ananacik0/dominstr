# Generated by Django 5.0.4 on 2024-05-12 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_category_tool_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop_app.category'),
        ),
    ]
