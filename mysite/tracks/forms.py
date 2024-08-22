from .models import Tracks
from django.forms import ModelForm, TextInput, DateInput, DateTimeInput, TextInput, Textarea

class TracksForm(ModelForm):
    class Meta:
        model = Tracks
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст песни'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }