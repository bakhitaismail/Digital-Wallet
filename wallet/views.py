from django.shortcuts import render
from .forms import AccountRegistration, CardRegistration, CurrencyRegistration, CustomerRegistration, LoanRegistration, NotificationRegistration, ReceiptRegistration, RewardRegistration, ThirdpartyRegistration, TransactionRegistration, WalletRegistration

# Create your views here.
def register_customer(request):
    form = CustomerRegistration()
    return render(request, "wallet/register_customer.html", {"form": form})

def register_wallet(request):
    form = WalletRegistration()
    return render(request, "wallet/register_wallet.html", {"form": form})

def register_account(request):
    form = AccountRegistration()
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