# Generated by Django 2.2.23 on 2021-05-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_code', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products_images')),
            ],
        ),
    ]
