from .models import films
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
	class Meta:
		model = films
		fields = ['title', 'short_description', 'text']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок фильма'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'})
		}