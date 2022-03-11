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

class Expenses(models.Model):
    id_expense = models.AutoField(primary_key=True, null=False, unique=True, verbose_name='ID Expense')
    ch_name = models.CharField(verbose_name='Name', max_length=100)
    ch_description = models.CharField(verbose_name='Description', max_length=500)
    b_State = models.BooleanField(verbose_name='State')
    dt_Start_Date = models.DateTimeField(verbose_name='Start Date')
    fk_expenses_account = models.ForeignKey(Expenses_Account, on_delete=models.CASCADE, verbose_name='FK Expenses')
    
    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'
        db_table = 'tbl_Expenses'

    def __str__(self):
        return str(self.id_expense)
