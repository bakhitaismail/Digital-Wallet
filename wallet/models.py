import email
from json.encoder import INFINITY
from locale import currency
from inspect import stack
from operator import countOf
from re import T
# from operator import mod
# from pyexpat import model
from xmlrpc.client import Boolean
from django.db import models
from django.utils import timezone
# from pytz import timezone
# import pytz

# Create your models here.
class Customer(models.Model):
    first_name= models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    GENDER_CHOICE=(("M", "Male"), ("F", "Female"))
    gender=models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)
    address=models.TextField(max_length=50)
    age=models.PositiveSmallIntegerField()
    # NATIONALITY_CHOICE=(("Kenya"), ("Tanzania"), ("Sudan"), ("Uganda"), ("Rwanda"), ("Canada"))
    nationality=models.CharField(max_length=20, null=True)
    id_number=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=35)
    profile_pic=models.ImageField
    country=models.CharField(max_length=30)
    signature=models.TextField()
    EMPLOYMENT_CHOICE=(("Engineer"), ("Doctor"), ("Farmer"), ("Teacher"))
    employment_status=models.CharField(max_length=15, null=True)
    marital_choice=(("Married"), ("Single"), ("Divorced"), ("Widow"), ("Widower"))
    marital_status=models.CharField(max_length=15, null=True)

class Wallet(models.Model):
    customer=models.ForeignKey("Customer", on_delete=models.CASCADE,related_name="Wallet_customer")
    amount=models.IntegerField()
    isactive=models.CharField(max_length=15)
    balance=models.IntegerField()
    pin=models.TextField(max_length=15)
    date=models.DateTimeField()
    currency=models.ForeignKey("Currency", on_delete=models.CASCADE,related_name="Wallet_currency")
    
class Account(models.Model):
    account_name=models.CharField(max_length=20)
    account_type=models.CharField(max_length=15)
    savings=models.IntegerField() 
    wallet=models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name="Account_wallet")
    destination=models.CharField(max_length=35)
    
class Transaction(models.Model):
    date=models.DateTimeField()
    amount=models.PositiveIntegerField()
    transaction_type=models.CharField(max_length=10)
    customer=models.ForeignKey("Customer", on_delete=models.CASCADE,related_name="Transaction_customer")
    transaction_code=models.CharField(max_length=4)
    charge=models.IntegerField()
    status=models.CharField(max_length=10)
    destination=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Transaction_destination")
    origin_account=models.CharField(max_length=140, default='STRING')
    
    
class Card(models.Model):
    card_number=models.CharField(max_length=16)
    card_name=models.CharField(max_length=20)
    account=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Card_account")
    pin_number=models.CharField(max_length=4)
    serial_code=models.PositiveSmallIntegerField()
    expiry_date=models.DateTimeField()
    card_status=models.CharField(max_length=10)
    
    
class Thirdparty(models.Model):
    fullname=models.CharField(max_length=20)   
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    transaction_cost=models.IntegerField()
    currency=models.ForeignKey("Currency", on_delete=models.CASCADE,related_name="Thirdparty_currency")
    isactive=models.BooleanField()
    account=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Thirdparty_account")
    
    
class Notification(models.Model):
    date_created=models.DateTimeField()
    isactive=models.BooleanField()
    recipient=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Notification_recipient")
    message=models.CharField(max_length=100)   
    
    
class Receipt(models.Model):
    receipt_date=models.DateTimeField()
    transaction=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Receipt_transaction")
    receipt_file=models.FileField()
    
 
class Loan(models.Model):
    loan_type=models.CharField(max_length=10)
    amount=models.IntegerField()
    wallet=models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name="Loan_wallet")
    date_and_time=models.DateTimeField()
    loan_terms=models.CharField(max_length=10)
    payment_due_date=models.DateTimeField()
    guarantor=models.CharField(max_length=15)
    balance=models.IntegerField()
    duration=models.CharField(max_length=10)
    interest_rates=models.IntegerField()
    status=models.CharField(max_length=10)
    
    
class Reward(models.Model):
    date_of_reward=models.DateTimeField()
    points=models.IntegerField()
    transaction=models.ForeignKey("Transaction", on_delete=models.CASCADE,related_name="Reward_transaction")
    Wallet=models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name="Reward_wallet")
    
    
class Currency(models.Model):
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=40)
    symbol=models.CharField(max_length=15)    