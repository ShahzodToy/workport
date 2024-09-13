from django.urls import path
from .views import PostView,ServiceView,OrderView,PricePlanView,CommentView,PortfolioWorkView


urlpatterns = [
    path('post',PostView.as_view(),name='post_get_or_create'),
    path('service',ServiceView.as_view()),
    path('order',OrderView.as_view()),
    path('priceplan',PricePlanView.as_view()),
    path('comment',CommentView.as_view()),
    path('portfolio',PortfolioWorkView.as_view())
]