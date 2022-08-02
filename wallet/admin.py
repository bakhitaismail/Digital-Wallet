from django.contrib import admin

from wallet.models import Customer

from .models import (Customer, Wallet, Account, Transaction, Card, Thirdparty, Notification, Receipt, Loan, Reward, Currency)

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "email",)
    search_fields=("first_name", "last_name",)
admin.site.register(Customer, CustomerAdmin)    
admin.site.register(Wallet)      
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Currency)