# Generated by Django 3.0.7 on 2020-07-22 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='size',
            new_name='product_size',
        ),
    ]
