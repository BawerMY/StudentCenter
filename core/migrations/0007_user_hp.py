# Generated by Django 4.1.7 on 2023-03-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_message_chat_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hp',
            field=models.IntegerField(default=0),
        ),
    ]
