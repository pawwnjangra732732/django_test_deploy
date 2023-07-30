from django.contrib import admin
from django.urls import path,include
from .views import hello_world

urlpatterns = [
    path('test/',hello_world,name='test-api'),
]