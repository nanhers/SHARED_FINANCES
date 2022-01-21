from django.db import models

# Create your models here.
class Expenses_Account(models.Model):
    id_account = models.AutoField(primary_key=True, null=False, unique=True, verbose_name='ID Account')
    ch_name = models.CharField(verbose_name='Name', max_length=100)
    ch_description = models.CharField(verbose_name='Description', max_length=500)
    b_State = models.BooleanField(verbose_name='State')
    dt_Start_Date = models.DateTimeField(verbose_name='Start Date')
    dt_End_Date = models.DateTimeField(verbose_name='End Date')
    
    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        db_table = 'tbl_Expenses_Account'

    def __str__(self):
        return str(self.id_account)
