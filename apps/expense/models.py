from django.db import models
from apps.categories.models import EN_Categories, EN_SubCategories

class EN_Expenses(models.Model):
 category     = models.ForeignKey(EN_Categories,null=False,on_delete=models.PROTECT)
 sub_category = models.ForeignKey(EN_SubCategories,null=True,on_delete=models.PROTECT)
 date         = models.DateField(null=False)
 description  = models.CharField(max_length=100, null=True)
 amount       = models.BigIntegerField(null=False)

 class meta:
     db_table="en_expenses"