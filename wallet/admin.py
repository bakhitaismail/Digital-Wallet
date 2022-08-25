from django.contrib import admin
from wallet.models import Customer
from .models import (Customer, Wallet, Account, Transaction, Card, Thirdparty, Notification, Receipt, Loan, Reward, Currency)

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "email",)
    search_fields=("first_name", "last_name")
admin.site.register(Customer, CustomerAdmin) 


class WalletAdmin(admin.ModelAdmin):
    list_display=("customer", "amount", "isactive",)
    search_fields=("customer", "amount")   
admin.site.register(Wallet,WalletAdmin)  

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name", "account_type", "savings",)
    search_fields=("account_name", "account_type")     
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("date", "amount", "transaction_type", "origin_account",)
    search_fields=("date", "amount")  
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_number", "card_name", "account",)
    search_fields=("card_number", "card_name")  
admin.site.register(Card, CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("fullname", "email", "phone_number",)
    search_fields=("fullname", "email",)  
admin.site.register(Thirdparty, ThirdpartyAdmin)
class NotificationAdmin(admin.ModelAdmin):
    list_display=("date_created", "isactive", "recipient",)
    search_fields=("date_created", "isactive")  
admin.site.register(Notification, NotificationAdmin)
class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_date", "transaction", "receipt_file",)
    search_fields=("receipt_date", "transaction")  
admin.site.register(Receipt, ReceiptAdmin)
class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type", "amount", "wallet",)
    search_fields=("loan_type", "amount")  
admin.site.register(Loan, LoanAdmin)
class RewardAdmin(admin.ModelAdmin):
    list_display=("date_of_reward", "points", "transaction",)
    search_fields=("date_of_reward", "points")  
admin.site.register(Reward,RewardAdmin)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=("name", "country", "symbol",)
    search_fields=("name", "country")  
admin.site.register(Currency, CurrencyAdmin)
