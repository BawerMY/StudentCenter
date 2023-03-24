from django.urls import path, include
from core import views

urlpatterns = [
    path('users/', views.UsersView.as_view()),
    path('users/<int:pk>', views.UsersView.as_view()),
    path('singup/', views.SingUpView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('me/', views.MeView.as_view()),

    path('chats/', views.ChatView.as_view()),
    path('chats/<int:pk>', views.ChatView.as_view()),
    path('me/chats/<int:pk>', views.ChatUpdateDestroyView.as_view()),
    path('me/chats/', views.MeChatView.as_view()),

    
    path('message/', views.MessageCreateView.as_view()),

]