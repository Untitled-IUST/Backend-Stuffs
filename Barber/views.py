from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from .models import Barber, Comment
from Auth.models import Barber as BarberModel_Auth 
from .serializers import BarberSerializer, BarberWithCommentsSerializer



class BarberView(RetrieveAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer

# Consider other fields of 
class BarberDetail(ListCreateAPIView):
    # model= BarberModel_Auth
    queryset = BarberModel_Auth.objects.all() #applied no filters yet!
    serializer_class = BarberWithCommentsSerializer
    # def get_queryset(self):
    #     data = super().get_queryset()
    #     comments = data.comments
    #     return comments
    
    # def get_context_data(self , **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     connected_comments = Comment.objects.filter(CommentPost=self.get_object())
    #     number_of_comments = connected_comments.count()
    #     data['comments'] = connected_comments
    #     data['no_of_comments'] = number_of_comments
        # data['comment_form'] = CommentForm()
    