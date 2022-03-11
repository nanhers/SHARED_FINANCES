from django.db import models
from account.models import Expenses_Account

# Create your models here.
class Expense(models.Model):
    id_expense = models.AutoField(primary_key=True, null=False, unique=True, verbose_name='ID Expense')
    ch_name = models.CharField(verbose_name='Name', max_length=100)
    ch_description = models.CharField(verbose_name='Description', max_length=500)
    b_State = models.BooleanField(verbose_name='State')
    dt_Start_Date = models.DateTimeField(verbose_name='Start Date')
    fk_Expense_account =models.ForeignKey(Expenses_Account, verbose_name='Expense Account')
    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'
        db_table = 'tbl_Expenses'

    def __str__(self):
        return str(self.id_expense)