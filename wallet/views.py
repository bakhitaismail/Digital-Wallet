from cgitb import html
from urllib import request
from django.shortcuts import render

from wallet.models import Customer
from .forms import AccountRegistration, CardRegistration, CurrencyRegistration, CustomerRegistration, LoanRegistration, NotificationRegistration, ReceiptRegistration, RewardRegistration, ThirdpartyRegistration, TransactionRegistration, WalletRegistration

# Create your views here.
def register_customer(request):
    if request.method=="POST":
       form = CustomerRegistration(request.POST)
       if form.is_valid():
           form.save()
    else:
        form= CustomerRegistration()    
    return render(request, "wallet/register_customer.html", {"form": form})

def register_wallet(request):
    if request.method=="POST":
       form = WalletRegistration(request.POST)
       if form.is_valid():
           form.save()
    else:
        form= WalletRegistration()       
    return render(request, "wallet/register_wallet.html", {"form": form})

def register_account(request):
    if request.method=="POST":
       form = AccountRegistration(request.POST)
       if form.is_valid():
           form.save()
    else:
        form=AccountRegistration()       
    return render(request, "wallet/register_account.html", {"form": form})

def register_transaction(request):
    form= TransactionRegistration()
    return render(request, "wallet/register_transaction.html", {"form":form})

def register_card(request):
    form= CardRegistration()
    return render(request, "wallet/register_card.html", {"form": form})

def register_thirdparty(request):
    form= ThirdpartyRegistration()
    return render(request, "wallet/register_thirdparty.html", {"form":form})

def register_notification(request):
    form= NotificationRegistration()
    return render(request, "wallet/register_notification.html", {"form":form})

def register_receipt(request):
    form= ReceiptRegistration()
    return render(request, "wallet/register_receipt.html", {"form":form})

def register_loan(request):
    form= LoanRegistration()
    return render(request, "wallet/register_loan.html", {"form":form})

def register_reward(request):
    form= RewardRegistration()
    return render(request, "wallet/register_reward.html", {"form":form})

def register_currency(request):
    form= CurrencyRegistration()
    return render(request, "wallet/register_currency.html", {"form":form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request, "wallet/list_customers.html", {"customers":customers})

def customer_profile(request, id):
    customer=Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html", {"customer":customer})

def edit_customer(request, id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistration(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id)
        
    else:
        form=CustomerRegistration(instance=customer)
        return render(request, "wallet/edit_customer.html", {"form":form})