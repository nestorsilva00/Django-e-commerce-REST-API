from django.db import models

class Cart_Item(models.Model):
    id=models.AutoField(primary_key=True)
    session_id=models.ForeignKey('session.Session', on_delete=models.CASCADE)
    product_id=models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='cart_item'
        verbose_name_plural='Cart Items'
