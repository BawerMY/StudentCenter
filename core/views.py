from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import login, logout
from .models import *
from .serializer import *

class UsersView(APIView):
    def get(self, request, *args, **kwargs):
        if(kwargs): users = User.objects.filter(pk=kwargs['pk'])
        else: users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class SingUpView(APIView):
    def get(self, request):
        return Response({
            "username": "username",
            "email": "email",
            "password": "password"
        })
    def post(self, request, format=None):
        serializer = SingUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data, request)
            if user:
                serializer = LoginSerializer(data=request.data)
                user = serializer.login(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def get(self, request):
        return Response({
            'username': 'username',
            'password': 'password',
        })
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.login(request.data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class MeView(APIView):
    def post(self, request, format=None):
        serializer = MeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(request.data, request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)





class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        if(kwargs): chats = Chat.objects.filter(pk=kwargs['pk'])
        else: chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ChatCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(request.data, request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class ChatUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatCreateSerializer
    def get_queryset(self):
        return self.request.user.chats

class MeChatView(generics.ListAPIView):
    serializer_class = ChatCreateSerializer
    def get_queryset(self):
        return self.request.user.chats



class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)