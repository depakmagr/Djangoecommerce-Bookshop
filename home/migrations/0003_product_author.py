# Generated by Django 4.1.5 on 2023-01-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
