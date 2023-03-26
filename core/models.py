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




class Question(Chat):
    answered = models.BooleanField(default=False)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages') # will be set default: default=User.objects.get(username = 'DELETED_USER')
    message = models.TextField(max_length=10000)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messagesR')
    
    def __str__(self) -> str:
        return f"[{self.chat}][{self.user}][{self.pk}] {self.message}"




# class PrivateChat(models.Model):
#     user1 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='private_chats1')
#     user2 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='private_chats2')
#     def messages(self):
#         msgs = []
#         for msg in self.private_messagesR.all():
#             m = PrivateMessage.objects.get(id=msg.id)
#             msgs.append({
#                 'user': m.user.username,
#                 'message': m.message,
#                 'chat': m.chat.pk,
#                 'id': msg.id
#             })
#         return msgs

# class PrivateMessage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_messages') # will be set default: default=User.objects.get(username = 'DELETED_USER')
#     message = models.TextField(max_length=10000)
#     chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE, related_name='private_messagesR')
    
#     def __str__(self) -> str:
#         return f"{self.chat} {self.chat.user1}-{self.chat.user2}"





