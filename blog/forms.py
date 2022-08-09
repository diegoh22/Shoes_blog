
from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


"""
Please note code was used from the Code Institute I Think Therefore I Blog
tutorial to help create this project.
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('likes',)
        widgets = {
            'content': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

