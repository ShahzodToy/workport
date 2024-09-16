from django.shortcuts import render
from .api.serializers import *
from rest_framework.views import APIView
from .models import *
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .api.serializers import PostSerializer, ServiceSerializer,OrderSerializer,CommentSerializer
from rest_framework import generics
from rest_framework import filters
from django.db import IntegrityError
from django.utils.translation import gettext as _

class PostView(APIView):
    permission_classes = (AllowAny, )

    def get(self,request):
        get_all = Post.objects.all()
        serializer = PostSerializer(get_all, many=True)
        
        data = {
            'posts':serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)
    
class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request,pk):
        post = self.get_object(pk)
        comment_post = CommentPost.objects.filter(post__id = pk)
        comment_serialzer = CommentPostSerializer(comment_post,many=True)
        post_serializer = PostSerializer(post)
        category_count = CategoryPost.objects.annotate(post_count=Count('post')).values('title', 'post_count')

        data = {
            'posts':post_serializer.data,
            'comments':comment_serialzer.data,
            'category':category_count
        }

        return Response(data, status=status.HTTP_200_OK)
    
class PostAPIView(generics.ListCreateAPIView):
    search_fields = ['title','desc']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


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


class LikeButtonView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LikeSerializer

    def get_queryset(self,pk):
        post_id = Post.objects.get(id=pk)
        like_post = LikePost.objects.create(
            post = post_id
        )
        return like_post
    
class CommentPostView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CommentPostSerializer

    def get_queryset(self,pk):
        post_id = Post.objects.get(id=pk)
        like_post = CommentPost.objects.create(
            post = post_id
        )
        return like_post
        

class NewsSubscribeView(APIView):
    def post(self, request):
        # Validate the incoming data
        if not request.data:
            return Response({"message": "Request body cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = NewsSubscribeSerializer(data=self.request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data.get('email')

        try:
            # Try to create a new subscription
            NewsLetterSubs.objects.create(email=email)
            return Response({"message": "Subscription successful", "email": email}, status=status.HTTP_201_CREATED)
        
        except IntegrityError:
            # If email already exists, return an error message
            return Response({"message": "This email is already subscribed."}, status=status.HTTP_400_BAD_REQUEST)
    
    
class PortfolioDetailView(APIView):
    def get(self,request,pk):
        portfolio_id = Portfolio.objects.filter(id = pk)
        comment_id = Comments.objects.filter(portfolio__id = pk)

        serializers_portfiloi = PortfoliWorkSerializer(portfolio_id,many=True)

        serializers_comment = CommentSerializer(comment_id,many=True)

        data = {
            'portfolio_work':serializers_portfiloi.data,
            'project_detail':serializers_comment.data
        }
        return Response(data,status=status.HTTP_200_OK)

    
class ContactView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContacSerializer
    queryset = ContactUser.objects.all()
