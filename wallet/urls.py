from django.urls import path
from .views import register_account, register_customer, register_transaction, register_wallet, register_card, register_thirdparty, register_notification, register_receipt, register_loan, register_reward, register_currency

urlpatterns =[
    path("register/", register_customer, name="register"),
    path("getwallet/", register_wallet, name="wallet"),
    path("accountregister/", register_account, name="account"),
    path("transactionregister/", register_transaction, name="transaction"),
    path("cardregister/", register_card, name="card"),
    path("thirdpartyregister/", register_thirdparty, name="thirdparty"),
    path("notificationregister/", register_notification, name="notification"),
    path("receiptregister/", register_receipt, name="receipt"),
    path("loanregister/", register_loan, name="loan"),
    path("rewardregister/", register_reward, name="reward"),
    path("currencyregister/", register_currency, name="currency"),
]
