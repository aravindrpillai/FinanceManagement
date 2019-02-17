from django.db import models

class EN_Users(models.Model):
 name     = models.CharField(max_length=25,null=False)
 username = models.CharField(max_length=25,unique=True,null=False,)
 password = models.CharField(max_length=25, null=False)
 email    = models.EmailField(max_length=25,null=False)

 class meta:
     db_table="en_users"