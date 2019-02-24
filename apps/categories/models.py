from django.db import models
from apps.userregistration.models import EN_Users

class EN_Categories(models.Model):
 name = models.CharField(max_length=25,null=False)
 user = models.ForeignKey(EN_Users, null=False, on_delete=models.CASCADE)
 retired = models.BooleanField(null=False, default=False)

 class meta:
     db_table="en_categories"
     unique_together = ('name', 'user')


class EN_SubCategories(models.Model):
 name = models.CharField(max_length=25,null=False)
 category = models.ForeignKey(EN_Categories, null=False, on_delete=models.PROTECT)
 user = models.ForeignKey(EN_Users, null=False, on_delete=models.CASCADE)
 retired = models.BooleanField(null=False, default=False)

 class meta:
     db_table="en_sub_categories"
     unique_together = ('name', 'category','user')
