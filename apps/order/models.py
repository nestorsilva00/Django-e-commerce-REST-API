from django.db import models

class Order(models.Model):
    PENDING_STATE = 'P'
    COMPLETED_STATE = 'C'

    ORDER_CHOICES= ((PENDING_STATE, "pending"), (COMPLETED_STATE, "completed"))

    id=models.AutoField(primary_key=True)
    order_number=models.CharField(max_length=200,unique=True)
    user_id=models.ForeignKey('user.User',on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    status=models.CharField(max_length=1, choices=ORDER_CHOICES, default=PENDING_STATE)
    payment_details_id=models.ForeignKey('Order_Payment_Detail',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='order'
        verbose_name_plural='Orders'

class Order_Payment_Detail(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_provider_id=models.ForeignKey('payment.Payment_Provider', on_delete=models.CASCADE)
    account_number=models.CharField(max_length=200)
    expiry_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='order_payment_details'
        verbose_name_plural='Order Payment Details'

class Order_Item(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id=models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='order_item'
        verbose_name_plural='Order Items'