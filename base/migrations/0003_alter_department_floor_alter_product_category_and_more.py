# Generated by Django 5.1.3 on 2024-11-15 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_department_productcategory_vendor_product_sell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='floor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.productcategory'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='department',
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.vendor'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='customer_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(to='base.department'),
        ),
    ]