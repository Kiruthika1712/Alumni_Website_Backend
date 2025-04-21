from datetime import timedelta
from django.utils import timezone
import secrets
from django.db import models

class mailVerification(models.Model):
    email = models.EmailField(primary_key=True)
    otp = models.CharField(max_length=6, default=secrets.token_hex(3))
    is_verified = models.BooleanField(default= False)
    otp_created_at= models.DateTimeField(auto_now_add=True)
    otp_expires_at= models.DateTimeField(blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at= models.DateTimeField(db_index= True,default=timezone.now()+timedelta(days=1), editable =False)







    