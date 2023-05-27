from django.urls import path
from .views import CustomerProfileView,WalletView, CustomerTransactionView
from rest_framework import routers



router = routers.SimpleRouter()
router.register('profile',CustomerProfileView,basename='profile')
router.register('wallet',WalletView,basename='wallet')

urlpatterns = [   
               path('transactions/', CustomerTransactionView.as_view(), name='customer_transactions'),
               ]+router.urls