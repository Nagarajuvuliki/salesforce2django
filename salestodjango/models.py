from django.db import models
from django.db.models.fields import CharField
class Testng(models.Model):
    Name=models.CharField(max_length=255,null=True)
    Email=models.CharField(max_length=200, null=True)
    class Meta:
        db_table = "Testing"
class SfUsers(models.Model):
    Username=models.CharField(max_length=255,null=True)
    FirstName=models.CharField(max_length=255,null=True)
    LastName=models.CharField(max_length=255,null=True)
    Email=models.CharField(max_length=200, null=True)
    class Meta:
        db_table = "SfUser"
class Contact(models.Model):
    Name=models.CharField(max_length=255,null=True)
    Email=models.CharField(max_length=200, null=True)
    AccountID=models.CharField(max_length=255,null=True)
    Phone=models.CharField(max_length=200, null=True)
    class Meta:
        db_table = "Contact"
class Account(models.Model):
    AccountNumber=models.CharField(max_length=255,null=True)
    LastActivityDate=models.CharField(max_length=255, null=True)
    AnnualRevenue=models.CharField(max_length=255,null=True)
    Name=models.CharField(max_length=200, null=True)
    class Meta:
        db_table = "Account"
