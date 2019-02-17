from django.db import models
# ENTITY : LOGIN CREDENTIALS
# Create your models here.
class EN_UserRegistration(models.Model):
 name     = models.CharField(max_length=25,null=False)
 username = models.CharField(max_length=25,unique=True,null=False,)
 password = models.CharField(max_length=25, null=False)
 emailaddress = models.EmailField(max_length=25,null=False,unique=True)
 class meta:
     db_table="EN_UserRegistration"