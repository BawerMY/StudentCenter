from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'hp', 'first_name', 'last_name']
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def login(self, data):
#         user = authenticate(username=data['username'], password=data['password'])
#         if not user: return {'ValidationError': "user/password doesn't maches"}
#         return user

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, data):
        user = User.objects.create_user(data['username'], data['email'], data['password'])
        user.save()
    # def update(self, data, request):
    #     user = request.user
    #     user[data.key] = data.value
    #     user.save()

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']




class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'description', 'user', 'messages']
class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name']
    def create(self, data, user):
        if data['type'] == 'chat': chat = Chat(name=data['name'], description=data['description'], user=user)
        if data['type'] == 'question': chat = Question(name=data['name'], description=data['description'], user=user)
        chat.save()
class UpdateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'description', 'name']
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message', 'chat']


# class CreatePrivateChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrivateChat
#         fields = ['user2']
# class PrivateChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrivateChat
#         fields = ['id', 'user1', 'user2', 'messages']
#     def create(self, data, user):
#         chat = PrivateChat(user1=user, user2=data['user2'])
#         chat.save()
# class PrivateMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrivateMessage
#         fields = ['message', 'chat']