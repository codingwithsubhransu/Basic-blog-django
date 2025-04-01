from rest_framework import serializers
from bloginterface.models import *
from django.contrib.auth.models import User


class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class loginserializer(serializers.Serializer):
    username = serializers.CharField(required= True)
    password = serializers.CharField(required= True, write_only= True)


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']