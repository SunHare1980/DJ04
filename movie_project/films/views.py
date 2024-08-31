from django.shortcuts import render, redirect
from .models import films
from .forms import News_postForm


def home(request):
    news = films.objects.all()
    return render(request, 'films/home.html', {'news': news})

def create_film(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"

    form = News_postForm()
    return render(request, 'films/add_new_film.html', {'form':form, 'error':error})