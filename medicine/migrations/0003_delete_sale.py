# Generated by Django 5.0.3 on 2024-04-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_rename_title_medicine_name_remove_medicine_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sale',
        ),
    ]