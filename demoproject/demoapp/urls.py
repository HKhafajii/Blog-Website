from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('drinks/<str:drinkName>/', views.drinks, name='drinks'),
    path('register/', views.register, name = 'register'),
]