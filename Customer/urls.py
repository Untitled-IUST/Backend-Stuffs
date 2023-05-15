from django.urls import path
from .views import CustomerProfileView,WalletView, CustomerTransactionView
from rest_framework import routers



router = routers.SimpleRouter()
router.register('profile',CustomerProfileView,basename='profile')
router.register('wallet',WalletView,basename='wallet')
# barber_router.register('images',views.BarberShopImagesView,basename='images')

urlpatterns = [
    # path("<int:pk>/transactions/", TransactionsView.as_view(), name="transactions"), 
    # path('transactions/<int:customer_id>/', CustomerTransactionView.as_view(), name='customer_transactions'),
    path('transactions/', CustomerTransactionView.as_view(), name='customer_transactions'),
    ] + router.urls