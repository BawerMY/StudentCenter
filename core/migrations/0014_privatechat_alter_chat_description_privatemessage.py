# Generated by Django 4.1.7 on 2023-03-25 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_chat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='private_chats', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='private_hats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='chat',
            name='description',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=10000)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_messagesR', to='core.privatechat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]