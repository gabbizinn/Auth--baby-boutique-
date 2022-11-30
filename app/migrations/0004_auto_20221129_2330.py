# Generated by Django 2.2.12 on 2022-11-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20221129_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Orders in the making', 'Orders in the making'), ('Out for delivery', 'Out for delivery'), ('Order delivered', 'Order delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]