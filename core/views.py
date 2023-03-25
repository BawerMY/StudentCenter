from rest_framework.authentication import SessionAuthentication, BasicAuthentication
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
        if(kwargs): users = User.objects.filter(pk=self.kwargs['pk'])
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
            user = serializer.create(request.data)
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
    def get(self, request):
        try:
            return Response({
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            })
        except: return Response({"error": "no logged in user"}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request, format=None):
        try:
            user = request.user
            if(request.data['key'] == 'username'): user.username = request.data['value']
            elif(request.data['key'] == 'email'): user.email = request.data['value']
            elif(request.data['key'] == 'first_name'): user.first_name = request.data['value']
            elif(request.data['key'] == 'last_name'): user.last_name = request.data['value']
            user.save()
            
            if(request.data['key'] == 'delete'): user.delete()
            return Response({
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
        }, status=status.HTTP_201_CREATED)
        except:
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
    serializer_class = UpdateChatSerializer

    def get_object(self, **kwargs):
        return Chat.objects.get(pk=kwargs['pk']) # not working
class MeChatView(generics.ListAPIView):
    serializer_class = ChatCreateSerializer
    def get_queryset(self):
        return self.request.user.chats

class MessageUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    def get_object(self):
        return self.request.user.messages
class MeMessageView(generics.ListAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        return self.request.user.messages


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)