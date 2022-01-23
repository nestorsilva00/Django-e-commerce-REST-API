from django.db import models

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'session'
        verbose_name_plural = 'Shopping Sessions'
