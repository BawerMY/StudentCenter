# Generated by Django 4.1.7 on 2023-03-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='description',
            field=models.CharField(default=None, max_length=10000),
        ),
    ]
