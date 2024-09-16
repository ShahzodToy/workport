from django.urls import path
from .views import (PostView,ServiceView,OrderView,PricePlanView,CommentView,
                            PortfolioWorkView,PostDetailView,
                            LikeButtonView,CommentPostView,PostAPIView,NewsSubscribeView,
                            PortfolioDetailView,ContactView)


urlpatterns = [
    path('post',PostView.as_view(),name='post_get_or_create'),
    path('service',ServiceView.as_view()),
    path('order',OrderView.as_view()),
    path('priceplan',PricePlanView.as_view()),
    path('comment',CommentView.as_view()),
    path('portfolio',PortfolioWorkView.as_view()),
    path('post-detail/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('like/<int:pk>',LikeButtonView.as_view()),
    path('comment/<int:pk>',CommentPostView.as_view()),
    path('search/',PostAPIView.as_view()),
    path('newsubscribe',NewsSubscribeView.as_view()),
    path('portfolio/<int:pk>',PortfolioDetailView.as_view()),
    path('contact',ContactView.as_view())

]