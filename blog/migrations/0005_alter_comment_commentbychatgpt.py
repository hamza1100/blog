# Generated by Django 4.2.8 on 2024-01-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_commentbychatgpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentByChatGPT',
            field=models.BooleanField(default=False),
        ),
    ]
