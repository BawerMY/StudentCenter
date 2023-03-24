from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    hp = models.IntegerField(default=0)

class Chat(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats') # will be set default: default=User.objects.get(username = 'DELETED_USER')
    description = models.TextField(max_length=10000, blank=True)
    def messages(self):
        msgs = []
        for msg in self.messagesR.all():
            m = Message.objects.get(id=msg.id)
            msgs.append({
                'user': m.user.username,
                'message': m.message,
                'chat': m.chat.pk,
                'id': msg.id
            })
        return msgs
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages') # will be set default: default=User.objects.get(username = 'DELETED_USER')
    message = models.TextField(max_length=10000)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messagesR')
    
    def __str__(self) -> str:
        return f"[{self.chat}][{self.user}][{self.pk}] {self.message}"




class Question(Chat):
    answered = models.BooleanField(default=False)
