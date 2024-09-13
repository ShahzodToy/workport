from rest_framework import serializers
from ..models import Post,Portfolio,Service,Order,PricePlan,Comments
from rest_framework.validators import ValidationError

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title','desc','img','category','date')


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

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)

