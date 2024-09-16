from django.contrib import admin
from .models import PricePlan,Service,Portfolio,Order,Comments,LikePost,CommentPost,CategoryPost,NewsLetterSubs,CategoryPortfolio,Post



for a in [PricePlan,Service,Portfolio,Comments,LikePost,CommentPost,CategoryPost,NewsLetterSubs,CategoryPortfolio,Post,Order]:
    admin.site.register(a)