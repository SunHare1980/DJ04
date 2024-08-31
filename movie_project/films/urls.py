from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_film', views.create_film, name='create_film')
]
