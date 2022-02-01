from django.contrib import admin
from django.urls import path, include
from .views import snippet_list
urlpatterns = [
    path('get-definition', snippet_list, name='get-definition')
]
