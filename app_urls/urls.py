from APIs.api.views import gamingAPI

from django.urls import path

urlpatterns = [
    path('', gamingAPI.as_view()),
]