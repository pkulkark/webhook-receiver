# Generated by Django 2.2.18 on 2021-02-09 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edx_shopify', '0004_unique_order_sku_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='ShopifyOrder',
        ),
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='ShopifyOrderItem',
        ),
    ]