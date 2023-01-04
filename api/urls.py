from . import views

from django.urls import path

urlpatterns = [
    path('', views.gamingAPI.as_view()),
    path('gameapi/<int:pk>/', views.gamingAPI.as_view()),
]