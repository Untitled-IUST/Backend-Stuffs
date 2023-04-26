from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Barber,Rate, Comment,Rating
from Customer.models import Customer
from Auth.models import User
from Auth.serializer import UserSerializer
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer, CommentSerializer, RatingSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist



class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    # permission_classes = [IsAuthenticated]
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     comments = Comment.objects.filter(barber=instance)
    #     comment_serializer = CommentSerializer(comments, many=True)
    #     return Response({
    #         'barber': serializer.data,
    #         'comments': comment_serializer.data,
    #     })
    # @action(methods=("PUT", "PATCH",), permission_classes=(IsAuthenticated,), detail=True)

    # @action(methods=["POST",], permission_classes=[IsAuthenticated], detail=True)
    # def add_comment(self, request):# *args, **kwargs):
    #     comment_author = Customer.objects.get(id= request.user.id)
        # comment_author = request.user.customer
        # try:
        #     # Get the current customer who is adding the comment
        #     comment_author = Customer.objects.get(id=request.user.id)
        # except ObjectDoesNotExist:
        #     return Response({"error": "Customer matching query does not exist."}, status=404)

        # comment_barber = self.get_object()
        # serializer = CommentSerializer(data=request.data, context=self.get_serializer_context())
        # serializer.is_valid(raise_exception=True)
        # # serializer.save(barber=self.get_object())
        # # return self.retrieve(request, *args, **kwargs)
        # serializer.save(customer=comment_author, barber=comment_barber)
        # return Response(serializer.data)        

        # if serializer.is_valid():
        #     text = serializer.data["body"]
        #     parent_comment = serializer.data["parent"]
        #     Comment.objects.create(customer=comment_author, barber=comment_barber,
        #                            body =text, parent_comment= parent_comment)


    @action(methods=["POST",], permission_classes=[IsAuthenticated], detail=True)
    def add_coment(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        serializer.save(barber=self.get_object())
        return self.retrieve(request, *args, **kwargs)
    @action(methods=["POST","PUT"], permission_classes=[IsAuthenticated], detail=True)
    def add_edit_rate(self, request, *args, **kwargs):
        if request.method == "POST":
                serializer = RatingSerializer(data=request.data, context=self.get_serializer_context())
                serializer.is_valid(raise_exception=True)
                serializer.save(barber=self.get_object())
                return self.retrieve(request, *args, **kwargs)
        # elif request.method == "PUT":
        #         rate = Rating.objects.get(barber=self.get_object(), customer=request.user.customer)
        #         serializer = RatingSerializer(rating=rate, data=request.data, context=self.get_serializer_context())
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save()
        #         return self.retrieve(request, *args, **kwargs)

class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        # baseInfo = User.objects.prefetch_related('barber_set').all()
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

# class AddComment(mode)
# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         (user, created) = User.objects.get_or_create(
#             id=request.user.id)
#         # baseInfo = User.objects.prefetch_related('user_set').all()
#         if request.method == 'GET':
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = UserSerializer(user, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)



# class BarberBaseProfileView(APIView):
#     def get(self,request):
#         queryset = User.objects.get(pk=request.user.id)
#         serializer = UserSerializer(queryset)
#         return Response(serializer.data)

#     def put(self,request):
#         user = User.objects.get(pk=request.user.id)
#         serializer = UserSerializer(user,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class BarberBaseProfileView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # lookup_fields = ['email', 'username']
        

# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return User.objects.prefetch_related('barber').all()







# class BarberBaseProfileView(ModelViewSet):
#     queryset = User.objects.prefetch_related('barber').all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         (barber, created) = User.objects.get(
#             barber=request.user.id)
#         # baseInfo = User.objects.prefetch_related('barber_set').all()
#         if request.method == 'GET':
#             serializer = UserSerializer(barber)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = UserSerializer(barber, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)















# class BarberShopImagesView(ModelViewSet):
#     serializer_class = BarberShopImagesSerializer

#     def get_serializer_context(self):
#         return {'barbershop_id':self.kwargs['barbershop_pk']}

#     def get_queryset(self):
#         return BarberShopImages.objects.filter(barbershop_id=self.kwargs['barbershop_pk'])



# class BarberView(ModelViewSet):
#     queryset = Barber.objects.all()
#     serializer_class = BarberSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
