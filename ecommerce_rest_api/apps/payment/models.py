from django.db import models

class Payment_Provider(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True) 
    deleted_at=models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table='payment_provider'
        verbose_name_plural='Payment Providers'
    
