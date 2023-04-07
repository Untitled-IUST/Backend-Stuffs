from django.shortcuts import render
from django.views import View
from rest_framework.generics import RetrieveUpdateAPIView 
from .models import CustomerProfile
from Auth.models import Customer
from .serializers import CustomerProfileSerializer
from django.contrib.auth.decorators import login_required
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
    #     return Customer.objects.filter(user=self.request.user)
        # if self.action == 'list':
        # return self.queryset
    # def update(self, request, *args, **kwargs):
        # return super().update(request, *args, **kwargs)
        
# class CustomerProfileView(View):
#     def get(self, request):
#         customers =CustomerProfile.objects.all()
#         return render(request, "dige chi", content_type="text") 