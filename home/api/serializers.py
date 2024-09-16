from rest_framework import serializers
from ..models import Post,Portfolio,Service,Order,PricePlan,Comments,LikePost,CommentPost,NewsLetterSubs,ContactUser
from rest_framework.validators import ValidationError
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    like_count = serializers.SerializerMethodField()
    comment_count= serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id','title','desc', 'img', 'category', 'tags', 'date', 'like_count','comment_count')

    def get_like_count(self,obj):
        return obj.count_like()
    
    def get_comment_count(self,obj):
        return obj.count_comment()
    
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = '__all__'
    

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikePost
        fields = '__all__'


class PortfoliWorkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Portfolio
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    def validate_user_name(self, data):
        if data.isdigit():
            return ValidationError({'message':'sorry, bro togirlab yoz jigar'})
        return data


class PricePlanserializer(serializers.ModelSerializer):

    class Meta:
        model = PricePlan
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

    # def create(self, validated_data):
    #     return Comments.objects.create(**validated_data)


class NewsSubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ContacSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUser
        fields = '__all__'
