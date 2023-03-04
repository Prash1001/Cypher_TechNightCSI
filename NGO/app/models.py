from django.db import models

# Create your models here.

class ngoModel(models.Model):
    ngo_name=models.CharField(max_length=50)
    ngo_reg_id=models.CharField(max_length=50)
    ngo_email=models.EmailField(max_length=50)
    phone_no=models.IntegerField()
    alt_phone_no=models.IntegerField()
    address_street1=models.CharField(max_length=50)
    address_street2=models.CharField(max_length=50)
    Country=models.CharField(max_length=50) #dropdown
    City=models.CharField(max_length=50)
    Region=models.CharField(max_length=50)
    Postal_code=models.IntegerField(max_length=15)
    ngo_domain=models.CharField(max_length=50) #dropdown
    