from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView,CreateAPIView
from .models import Barber, Comment
from Auth.models import Barber as BarberModel_Auth 
from .serializers import BarberSerializer, BarberWithCommentsSerializer, CommentSerializer,CommentSerializerOnPOST



class BarberView(RetrieveAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer



class BarberDetail(ListCreateAPIView):
    queryset = BarberModel_Auth.objects.all() #applied no filters yet!
    serializer_class = BarberWithCommentsSerializer
    
class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all() 
    # serializer_class = CommentSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializerOnPOST
        return CommentSerializer