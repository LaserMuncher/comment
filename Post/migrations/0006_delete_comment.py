# Generated by Django 4.2.4 on 2023-11-06 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
