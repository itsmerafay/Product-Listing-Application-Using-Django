# Generated by Django 5.0.1 on 2024-01-05 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='receipe_description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='receipe',
            old_name='receipe_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='receipe',
            old_name='receipe_name',
            new_name='product_name',
        ),
    ]
