from django.contrib import admin
from django.urls import path
from .views import person_list


urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('new/', person_list, name="person_new"),
]