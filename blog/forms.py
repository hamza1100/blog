from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['post']
        labels = {
            'username': 'Your Name',
            'user_email': 'Your Email',
            'commentByChatGPT': 'Generate Comment Using OpenAI',
            'text': 'Your Comment'
        }
