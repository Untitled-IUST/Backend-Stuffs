from django.shortcuts import render
from django.views import View
from rest_framework.generics import RetrieveUpdateAPIView 
from .models import CustomerProfile
from Auth.models import Customer
from .serializers import CustomerProfileSerializer

# Create your views here.


# class CustomerProfileView(View):
#     def get(self, request):
#         customers =CustomerProfile.objects.all()
#         return render(request, "dige chi", content_type="text")

class CustomerProfileView(RetrieveUpdateAPIView):
    # queryset = CustomerProfile.objects.all()
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    # def get_queryset(self):
        # if self.action == 'list':
            # return self.queryset.filter(user=self.request.user)
        # return self.queryset