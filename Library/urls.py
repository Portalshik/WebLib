from django.urls import path

from .views import index, add

urlpatterns = [
    path('', index),
    path('add/', add)
]
