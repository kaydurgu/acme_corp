# Generated by Django 5.0.6 on 2024-06-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(default=None, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default=None, max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='manufactured_date',
            field=models.DateField(auto_now=True),
        ),
    ]