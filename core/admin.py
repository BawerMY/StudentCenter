from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Question)
# admin.site.register(PrivateChat)
# admin.site.register(PrivateMessage)