from django.db import models
from django.db.models.base import ModelState


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='category'
        verbose_name_plural='Categories'

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    SKU=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    category_id=models.ManyToManyField(Category, related_name='category')
    discount_id=models.ForeignKey('Discount', on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='product'
        verbose_name_plural='Products'


class Product_Inventary(models.Model):
    id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='product_inventary'
        verbose_name_plural='Product Inventaries'


class Discount(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    discount_percentage=models.FloatField()
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='discount'
        verbose_name_plural='Discounts'

class Product_Image(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False, related_name='product_image')
    image=models.ImageField(upload_to='images/products/')
    description=models.CharField(max_length=150, null=True)
    color=models.CharField(max_length=20, null=False, blank=False)