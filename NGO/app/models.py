from django.db import models

# Create your models here.

class ngoModel(models.Model):
    ngo_name=models.CharField(max_length=50,null=True)
    ngo_reg_id=models.CharField(max_length=50)
    ngo_email=models.EmailField(max_length=50)
    phone_no=models.IntegerField()
    alt_phone_no=models.IntegerField()
    address_street1=models.CharField(max_length=50)
    address_street2=models.CharField(max_length=50)
    Country=models.CharField(max_length=50) #dropdown
    City=models.CharField(max_length=50)
    Region=models.CharField(max_length=50)
    Postal_code=models.IntegerField()
    ngo_domain=models.CharField(max_length=50) #dropdown
    

class volunteerModel(models.Model):
    volunteer_name=models.CharField(max_length=50,null=True)
    volunteer_email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    postalcode=models.IntegerField()
    education=models.CharField(max_length=50)
    domain=models.CharField(max_length=50)