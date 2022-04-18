from django.contrib import admin
from account.models import ExpensesAccount, Expenses

# Register your models here.
class ExpensesAccountAdmin(admin.ModelAdmin):
    list_display = ('id_account', 'ch_name', 'ch_description', 'b_State')
class ExpensesAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExpensesAccount, ExpensesAccountAdmin)
admin.site.register(Expenses, ExpensesAdmin)

