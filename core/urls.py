from django.urls import path, include
from core import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', views.UsersView.as_view()),
    path('users/<int:pk>', views.UsersView.as_view()),
    path('singup/', views.SingUpView.as_view()),
    # path('login/', views.LoginView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view()),
    path('me/', views.MeView.as_view()),

    path('chats/', views.ChatView.as_view()),
    path('chats/<int:pk>', views.ChatView.as_view()),
    path('me/chats/<int:pk>', views.ChatUpdateDestroyView.as_view()),
    path('me/chats/', views.MeChatView.as_view()),

    # path('chats/private/', views.PrivateChatView.as_view()),
    # path('chats/private/<int:pk>', views.PrivateChatView.as_view()),
    # path('message/private/', views.PrivateMessageView.as_view()),
    
    path('message/', views.MessageCreateView.as_view()),
    path('me/messages/', views.MeMessageView.as_view()),
    path('me/messages/<int:pk>', views.MessageUpdateDestroyView.as_view()),
]
