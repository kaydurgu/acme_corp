# Generated by Django 5.0.6 on 2024-06-11 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('EL', 'Electronics'), ('FA', 'Fashion'), ('HO', 'Home'), ('TO', 'Toys'), ('BO', 'Books'), ('SP', 'Sports'), ('BE', 'Beauty'), ('AU', 'Automotive'), ('GR', 'Grocery'), ('HE', 'Health'), ('OF', 'Office Supplies'), ('OT', 'Other')], default='OT', max_length=2)),
                ('manufactured_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('responsible_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible_worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
