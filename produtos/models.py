from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_code = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='products_images', null=True, blank=True)  # campo opcional

    def __str__(self):
        return self.product_name+'-'+self.product_code
