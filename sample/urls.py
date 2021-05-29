
from .views import viewcases
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',viewcases)
    #path('design/',viewcases)
]
