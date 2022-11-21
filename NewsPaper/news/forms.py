from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)
    text = forms.CharField(min_length=100)
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("title")
        description = cleaned_data.get("text")
        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )
        return cleaned_data