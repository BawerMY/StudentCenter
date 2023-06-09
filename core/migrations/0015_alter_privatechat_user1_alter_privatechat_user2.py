# Generated by Django 4.1.7 on 2023-03-25 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_privatechat_alter_chat_description_privatemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatechat',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='private_chats1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='privatechat',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='private_chats2', to=settings.AUTH_USER_MODEL),
        ),
    ]
