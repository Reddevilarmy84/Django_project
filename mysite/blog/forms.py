from .models import Artiсles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticleForm(ModelForm):
    class Meta:
        model = Artiсles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Анонс статьи',
            }),
            'full_text': Textarea(attrs={
                'class': 'input',
                'placeholder': 'Текст статьи',
            }),
            'date': DateTimeInput(attrs={
                'class': 'input',
                'placeholder': '2025-11-15 10:15:20'
            })
        }