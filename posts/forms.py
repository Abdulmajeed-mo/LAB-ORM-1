
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "image"]

        widgets = {
            "author": forms.TextInput(attrs={
                "placeholder": "Enter your name",
                "maxlength": "100"
            }),
            "title": forms.TextInput(attrs={
                "placeholder": "Give your story a title",
                "maxlength": "2048"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Every great story begins with a few words...",
                "rows": "9"
            }),
            "image": forms.FileInput(attrs={
                "accept": "image/*",
                "class": "upload-input"
            })
        }
