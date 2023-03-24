from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def login(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user: return {'ValidationError': "user/password doesn't maches"}
        return user

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, data):
        user = User.objects.create_user(data['username'], data['email'], data['password'])
        user.save()
    def update(self, data, request):
        user = request.user
        user[data.key] = data.value
        user.save()

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    # def update(self, data, request):
    #     user = request.user
    #     user[data.key] = data.value
    #     user.save()
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'description', 'user', 'messages']

class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['name', 'description', 'pk']
    def create(self, data, user):
        if data['type'] == 'chat': chat = Chat(name=data['name'], user=user)
        if data['type'] == 'question': chat = Question(name=data['name'], user=user)
        chat.save()



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message', 'chat']