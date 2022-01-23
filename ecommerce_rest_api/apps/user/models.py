from django.db import models

class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='user'
        verbose_name_plural='Users'

class User_Address(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1=models.CharField(max_length=500)
    address_line_2=models.CharField(max_length=500, null=True)
    city=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    residential_phone_number=models.CharField(max_length=100)

    class Meta:
        db_table='user_address'
        verbose_name_plural='User Addresses'

class User_Payment(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    payment_provider_id=models.ForeignKey('payment.Payment_Provider', on_delete=models.CASCADE)
    account_number=models.CharField(max_length=200)
    expiry_date=models.DateField()

    class Meta:
        db_table='user_payment'
        verbose_name_plural='User Payments'


