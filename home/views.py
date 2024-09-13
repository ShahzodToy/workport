from django.shortcuts import render
from .api.serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .api.serializers import PostSerializer, ServiceSerializer,OrderSerializer,CommentSerializer
from rest_framework import generics



class PostView(APIView):
    permission_classes = (AllowAny, )

    def get(self,request):
        get_all = Post.objects.all()
        serializer = PostSerializer(get_all, many=True)
        
        data = {
            'posts':serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)


class ServiceView(APIView):
    permission_classes = (AllowAny, )

    def get(self,request):
        servise = Service.objects.all()
        serializer  = ServiceSerializer(servise,many = True)

        return Response(serializer.data)
    

class OrderView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class PricePlanView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PricePlanserializer
    queryset =PricePlan.objects.all()
    


class CommentView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()


class PortfolioWorkView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PortfoliWorkSerializer
    queryset = Portfolio.objects.all()
    
    


    

